"""Dopasowanie zgłoszenia do kolejki albo odmowa, gdy żadna nie pasuje.

Model dostaje tylko temat i treść. Wynik i uzasadnienie zapisują się przy zgłoszeniu.
"""

import json
import os
import re
import threading
import urllib.error
import urllib.request

from app import db, repo

MODEL = os.environ.get("LLM_MODEL", "qwen3:8b")
BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:11434").rstrip("/")

_SCHEMA = {
    "type": "object",
    "properties": {
        "decision": {"type": "string", "enum": ["dopasowane", "brak"]},
        "category_code": {"type": "string"},
        "reasoning": {"type": "string"},
    },
    "required": ["decision", "category_code", "reasoning"],
}

_SYSTEM = """Klasyfikator helpdesku IT Meridian. Widzisz tylko temat i treść.
Wybierz jedną kolejkę (decision=dopasowane, category_code z listy) albo odmów (decision=brak, category_code=""), gdy tekst nie jest sprawą IT albo nie da się z niego wyczytać usterki.
Dwie pasujące kolejki to nie odmowa: wybierz lepszą, drugą wymień w uzasadnieniu.
Prośba o sprawdzenie poczty, VPN, drukarki albo dostępu jest dopasowaniem. Odmowa tylko wtedy, gdy tekst w ogóle nie jest sprawą dla IT.
Uzasadnienie po polsku, dwa krótkie akapity: cytat z treści, kolejki które odpadały, dlaczego ta decyzja.
Zwróć wyłącznie JSON."""


def classify_text(subject: str, body: str) -> dict:
    with db.connection() as conn:
        labels = repo.list_categories(conn)
    if not labels:
        return {
            "status": "brak",
            "category_code": None,
            "reasoning": "Nie ma żadnej kategorii, do której dałoby się dopasować zgłoszenie.",
            "model": MODEL,
        }
    codes = {item["code"] for item in labels}
    last_error: Exception | None = None
    for _attempt in range(2):
        try:
            return _interpret(_ask(subject, body, labels), codes)
        except (ValueError, json.JSONDecodeError) as exc:
            last_error = exc
    assert last_error is not None
    raise last_error


def _interpret(raw: str, codes: set[str]) -> dict:
    parsed = _parse(raw)
    decision = str(parsed.get("decision") or "").strip()
    code = str(parsed.get("category_code") or "").strip()
    reasoning = str(parsed.get("reasoning") or "").strip()
    if len(reasoning) < 40:
        raise ValueError("uzasadnienie jest za krótkie")
    if decision == "brak":
        return {"status": "brak", "category_code": None, "reasoning": reasoning, "model": MODEL}
    if decision == "dopasowane" and code in codes:
        return {"status": "dopasowane", "category_code": code, "reasoning": reasoning, "model": MODEL}
    raise ValueError(f"zła decyzja modelu: {decision!r} / {code!r}")


class Worker:
    def __init__(self) -> None:
        self._wake = threading.Event()
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._run, name="ai-dopasowanie", daemon=True)
        self._thread.start()
        self._wake.set()

    def stop(self) -> None:
        self._stop.set()
        self._wake.set()
        if self._thread:
            self._thread.join(timeout=2)

    def kick(self) -> None:
        self._wake.set()

    def _run(self) -> None:
        while not self._stop.is_set():
            self._wake.wait(5)
            if self._stop.is_set():
                return
            self._wake.clear()
            self._drain()

    def _drain(self) -> None:
        seen_failure: set[int] = set()
        while not self._stop.is_set():
            with db.connection() as conn:
                row = repo.next_unmatched(conn, skip_ids=seen_failure)
            if not row:
                return
            try:
                result = classify_text(row["subject"], row["body"])
            except urllib.error.HTTPError as exc:
                if exc.code >= 500:
                    print(f"Dopasowanie wstrzymane, model zwrócił {exc.code}.")
                    if self._stop.wait(15):
                        return
                    continue
                seen_failure.add(int(row["id"]))
                _mark_failed(row, exc)
                continue
            except urllib.error.URLError as exc:
                print(f"Dopasowanie wstrzymane, model niedostępny: {exc}")
                if self._stop.wait(15):
                    return
                continue
            except Exception as exc:
                seen_failure.add(int(row["id"]))
                print(f"Zgłoszenie {row['id']}: błąd dopasowania: {exc}")
                _mark_failed(row, exc)
                continue
            with db.connection() as conn:
                saved = repo.save_match(
                    conn,
                    int(row["id"]),
                    row["content_hash"],
                    status=result["status"],
                    category_code=result["category_code"],
                    reasoning=result["reasoning"],
                    model=result["model"],
                )
            if saved:
                label = result["category_code"] or "brak"
                print(f"Zgłoszenie {row['id']}: {result['status']} ({label})")


worker = Worker()


def _mark_failed(row: dict, exc: Exception) -> None:
    with db.connection() as conn:
        repo.save_match(
            conn,
            int(row["id"]),
            row["content_hash"],
            status="blad",
            category_code=None,
            reasoning=f"Nie udało się odczytać decyzji modelu: {exc}",
            model=MODEL,
        )


def _options() -> dict:
    options = {"temperature": 0.2, "num_predict": 420, "num_ctx": 3072}
    raw = os.environ.get("LLM_NUM_GPU")
    if raw not in (None, ""):
        options["num_gpu"] = int(raw)
    return options


def _ask(subject: str, body: str, labels: list[dict]) -> str:
    catalog = "\n".join(
        f"- {item['code']}: {item['name']}. {item['description']}" for item in labels
    )
    user = (
        "Kolejki:\n"
        f"{catalog}\n\n"
        f"Temat: {subject}\n\n"
        f"Treść:\n{body}"
    )
    payload = {
        "model": MODEL,
        "stream": False,
        "think": False,
        "format": _SCHEMA,
        "messages": [
            {"role": "system", "content": _SYSTEM},
            {"role": "user", "content": user},
        ],
        "keep_alive": "30m",
        "options": _options(),
    }
    request = urllib.request.Request(
        f"{BASE_URL}/api/chat",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        data = json.loads(response.read().decode())
    return str(data.get("message", {}).get("content") or "")


def _parse(raw: str) -> dict:
    text = raw.strip()
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    parsed = json.loads(text)
    if not isinstance(parsed, dict):
        raise ValueError("odpowiedź nie jest obiektem JSON")
    return parsed
