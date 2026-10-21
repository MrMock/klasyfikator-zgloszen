"""Przykładowe zgłoszenia. W bazie nie ma kategorii: temat i treść wystarczą modelowi."""

from datetime import datetime

from app.samples_clear import TICKETS as CLEAR_TICKETS
from app.samples_mixed import TICKETS as MIXED_TICKETS
from app.textutil import parse_created_at

TICKETS = CLEAR_TICKETS + MIXED_TICKETS


def validate() -> None:
    if len(TICKETS) != 100:
        raise ValueError(f"oczekiwano 100 zgłoszeń, jest {len(TICKETS)}")
    subjects = []
    bodies = []
    for index, ticket in enumerate(TICKETS, start=1):
        if set(ticket) != {"subject", "body", "created_at"}:
            raise ValueError(f"#{index} ma inne pola niż temat, treść i data")
        if len(ticket["subject"]) < 8 or len(ticket["body"]) < 100:
            raise ValueError(f"#{index} za krótkie: {ticket['subject']!r}")
        created = parse_created_at(ticket["created_at"])
        if not created:
            raise ValueError(f"#{index} zła data")
        moment = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
        if moment.weekday() >= 5 or not 7 <= moment.hour <= 16:
            raise ValueError(f"#{index} data poza czasem pracy: {created}")
        text = f"{ticket['subject']} {ticket['body']}".lower()
        if "po weekendzie" in text and moment.weekday() != 0:
            raise ValueError(f"#{index} „po weekendzie” nie wypada w poniedziałek")
        subjects.append(ticket["subject"])
        bodies.append(ticket["body"])
    if len(set(subjects)) != len(subjects):
        raise ValueError("powtórzony temat")
    if len(set(bodies)) != len(bodies):
        raise ValueError("powtórzona treść")


if __name__ == "__main__":
    validate()
    print(f"OK: {len(TICKETS)} zgłoszeń")
