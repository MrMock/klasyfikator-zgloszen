"""Baza zgłoszeń. Kategorię dopisuje model, nie formularz."""

import sqlite3
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "helpdesk.db"

SCHEMA = """
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at TEXT NOT NULL,
    search_blob TEXT NOT NULL DEFAULT '',
    content_hash TEXT NOT NULL DEFAULT '',
    ai_status TEXT NOT NULL DEFAULT 'oczekuje'
        CHECK (ai_status IN ('oczekuje', 'dopasowane', 'brak', 'blad')),
    ai_category_code TEXT,
    ai_reasoning TEXT NOT NULL DEFAULT '',
    ai_model TEXT NOT NULL DEFAULT ''
);

CREATE INDEX idx_tickets_created ON tickets (created_at);
CREATE INDEX idx_tickets_ai_status ON tickets (ai_status);
"""


def connect() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    # endpoint i dependency potrafią iść różnymi wątkami
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


@contextmanager
def connection():
    conn = connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init() -> None:
    with connection() as conn:
        if _legacy(conn):
            conn.execute("DROP TABLE IF EXISTS tickets")
            conn.execute("DROP TABLE IF EXISTS categories")
        exists = conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'tickets'"
        ).fetchone()
        if not exists:
            conn.executescript(SCHEMA)
        else:
            _ensure_ai_columns(conn)
        _ensure_categories(conn)
        _backfill_hashes(conn)


def _legacy(conn: sqlite3.Connection) -> bool:
    tables = {
        row[0]
        for row in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    }
    if "tickets" not in tables:
        return False
    columns = {row[1] for row in conn.execute("PRAGMA table_info(tickets)")}
    return bool(columns & {"author_name", "status", "category_id", "priority"})


def _ensure_ai_columns(conn: sqlite3.Connection) -> None:
    columns = {row[1] for row in conn.execute("PRAGMA table_info(tickets)")}
    if "content_hash" not in columns:
        conn.execute("ALTER TABLE tickets ADD COLUMN content_hash TEXT NOT NULL DEFAULT ''")
    if "ai_status" not in columns:
        conn.execute("ALTER TABLE tickets ADD COLUMN ai_status TEXT NOT NULL DEFAULT 'oczekuje'")
    if "ai_category_code" not in columns:
        conn.execute("ALTER TABLE tickets ADD COLUMN ai_category_code TEXT")
    if "ai_reasoning" not in columns:
        conn.execute("ALTER TABLE tickets ADD COLUMN ai_reasoning TEXT NOT NULL DEFAULT ''")
    if "ai_model" not in columns:
        conn.execute("ALTER TABLE tickets ADD COLUMN ai_model TEXT NOT NULL DEFAULT ''")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_tickets_ai_status ON tickets (ai_status)")


def _ensure_categories(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            code TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            sort_order INTEGER NOT NULL
        )
        """
    )
    count = conn.execute("SELECT COUNT(*) AS c FROM categories").fetchone()["c"]
    if count:
        return
    from app.labels import LABELS

    for index, item in enumerate(LABELS, start=1):
        conn.execute(
            """
            INSERT INTO categories (code, name, description, sort_order)
            VALUES (?, ?, ?, ?)
            """,
            (item["code"], item["name"], item["description"], index),
        )


def _backfill_hashes(conn: sqlite3.Connection) -> None:
    from app.textutil import content_hash

    rows = conn.execute(
        "SELECT id, subject, body FROM tickets WHERE content_hash = '' OR content_hash IS NULL"
    ).fetchall()
    for row in rows:
        conn.execute(
            "UPDATE tickets SET content_hash = ? WHERE id = ?",
            (content_hash(row["subject"], row["body"]), row["id"]),
        )
