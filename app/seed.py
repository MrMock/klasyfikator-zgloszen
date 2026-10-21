"""Wczytanie przykładowych zgłoszeń do bazy."""

import argparse

from app import db, repo
from app.seed_data import TICKETS, validate
from app.textutil import parse_created_at


def seed_if_empty() -> bool:
    db.init()
    with db.connection() as conn:
        if repo.count_tickets(conn):
            return False
        _insert_all(conn)
    return True


def reseed() -> None:
    db.init()
    with db.connection() as conn:
        conn.execute("DELETE FROM tickets")
        _insert_all(conn)


def _insert_all(conn) -> None:
    validate()
    for ticket in TICKETS:
        repo.insert_ticket(
            conn,
            {
                "subject": ticket["subject"],
                "body": ticket["body"],
                "created_at": parse_created_at(ticket["created_at"]),
            },
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Wczytaj przykładowe zgłoszenia.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Kasuje obecne zgłoszenia i wczytuje przykłady od nowa.",
    )
    args = parser.parse_args()
    if args.force:
        reseed()
        print("Wczytano od nowa 100 zgłoszeń.")
        return
    if seed_if_empty():
        print("Wczytano przykładowe dane: 100 zgłoszeń.")
        return
    print("Baza już ma zgłoszenia. Nic nie zmieniam.")
    print("Polecenie z --force kasuje je i wgrywa przykłady od nowa.")


if __name__ == "__main__":
    main()
