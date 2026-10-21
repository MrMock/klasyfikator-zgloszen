"""Walidacja formularza zgłoszenia."""

from datetime import datetime

from app.textutil import parse_created_at


def blank_ticket_form() -> dict:
    return {
        "subject": "",
        "body": "",
        "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M"),
    }


def ticket_to_form(ticket: dict) -> dict:
    return {
        "subject": ticket["subject"],
        "body": ticket["body"],
        "created_at": ticket["created_at"].replace(" ", "T")[:16],
    }


def parse_ticket(raw: dict) -> tuple[dict | None, str | None]:
    subject = " ".join(str(raw.get("subject") or "").split())
    body = str(raw.get("body") or "").strip()
    created = parse_created_at(str(raw.get("created_at") or ""))

    if len(subject) < 3:
        return None, "Temat musi mieć co najmniej 3 znaki."
    if len(subject) > 180:
        return None, "Temat może mieć najwyżej 180 znaków."
    if len(body) < 10:
        return None, "Treść musi mieć co najmniej 10 znaków."
    if len(body) > 8000:
        return None, "Treść może mieć najwyżej 8000 znaków."
    if created is None:
        return None, "Data zgłoszenia jest niepoprawna."

    return {"subject": subject, "body": body, "created_at": created}, None


def posted_ticket(raw: dict) -> dict:
    form = blank_ticket_form()
    form["subject"] = raw.get("subject") or ""
    form["body"] = raw.get("body") or ""
    if raw.get("created_at"):
        form["created_at"] = raw.get("created_at")
    return form


def blank_category_form() -> dict:
    return {"name": "", "code": "", "description": ""}


def posted_category(raw: dict) -> dict:
    return {
        "name": raw.get("name") or "",
        "code": raw.get("code") or "",
        "description": raw.get("description") or "",
    }


def parse_category(raw: dict) -> tuple[dict | None, str | None]:
    from app.textutil import CODE_RE, slugify

    name = " ".join(str(raw.get("name") or "").split())
    code = str(raw.get("code") or "").strip().lower()
    description = str(raw.get("description") or "").strip()
    if len(name) < 3:
        return None, "Nazwa kategorii musi mieć co najmniej 3 znaki."
    if len(name) > 80:
        return None, "Nazwa kategorii może mieć najwyżej 80 znaków."
    if len(description) < 10:
        return None, "Opis musi mieć co najmniej 10 znaków. Model czyta go przy dopasowaniu."
    if len(description) > 500:
        return None, "Opis może mieć najwyżej 500 znaków."
    if not code:
        code = slugify(name)
    if not CODE_RE.match(code) or len(code) > 48:
        return None, "Kod może zawierać małe litery, cyfry i myślniki."
    return {"name": name, "code": code, "description": description}, None
