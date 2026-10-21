"""Tekst zgłoszenia: data, wyszukiwanie i skrót do listy."""

import hashlib
import re
from datetime import datetime

_PL = str.maketrans(
    {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z",
    }
)

WEEKDAYS = [
    "poniedziałek",
    "wtorek",
    "środa",
    "czwartek",
    "piątek",
    "sobota",
    "niedziela",
]

_DATE_FORMATS = (
    "%Y-%m-%dT%H:%M",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d %H:%M:%S",
)

CODE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def normalize(value: str) -> str:
    folded = value.casefold().translate(_PL)
    return " ".join(folded.split())


def search_blob(subject: str, body: str) -> str:
    return normalize(f"{subject}\n{body}")


def content_hash(subject: str, body: str) -> str:
    return hashlib.sha256(f"{subject}\n{body}".encode()).hexdigest()


def like_pattern(query: str) -> str:
    text = normalize(query)
    text = text.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    return f"%{text}%"


def slugify(value: str) -> str:
    text = normalize(value)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return (text or "kategoria")[:48]


def parse_created_at(value: str) -> str | None:
    raw = (value or "").strip()
    for fmt in _DATE_FORMATS:
        try:
            parsed = datetime.strptime(raw, fmt)
        except ValueError:
            continue
        return parsed.strftime("%Y-%m-%d %H:%M:%S")
    return None


def _parsed(value: str) -> datetime | None:
    canonical = parse_created_at(value) if value else None
    if not canonical:
        return None
    return datetime.strptime(canonical, "%Y-%m-%d %H:%M:%S")


def format_dt(value: str) -> str:
    parsed = _parsed(value)
    if not parsed:
        return value or ""
    return parsed.strftime("%d.%m.%Y %H:%M")


def format_dt_long(value: str) -> str:
    parsed = _parsed(value)
    if not parsed:
        return value or ""
    weekday = WEEKDAYS[parsed.weekday()]
    return f"{weekday}, {parsed.strftime('%d.%m.%Y %H:%M')}"


def format_dt_input(value: str) -> str:
    parsed = _parsed(value)
    if not parsed:
        return ""
    return parsed.strftime("%Y-%m-%dT%H:%M")


def preview(value: str, limit: int = 140) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"
