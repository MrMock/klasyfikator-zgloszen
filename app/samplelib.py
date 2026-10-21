"""Wspólna konstrukcja przykładowego zgłoszenia: temat, treść, data."""


def z(subject: str, body: str, created_at: str) -> dict:
    return {
        "subject": " ".join(subject.split()),
        "body": body.strip(),
        "created_at": created_at,
    }
