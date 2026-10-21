"""Odczyt i zapis zgłoszeń."""

import sqlite3

from app.textutil import content_hash, like_pattern, search_blob

_TICKET_COLUMNS = """
    id, subject, body, created_at, content_hash,
    ai_status, ai_category_code, ai_reasoning, ai_model
"""


def _all(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> list[dict]:
    return [dict(row) for row in conn.execute(sql, params).fetchall()]


def _one(conn: sqlite3.Connection, sql: str, params: tuple = ()) -> dict | None:
    row = conn.execute(sql, params).fetchone()
    return dict(row) if row else None


def list_tickets(conn: sqlite3.Connection, query: str = "") -> list[dict]:
    sql = f"SELECT {_TICKET_COLUMNS} FROM tickets WHERE 1 = 1"
    params: list[str] = []
    if query.strip():
        sql += " AND search_blob LIKE ? ESCAPE '\\'"
        params.append(like_pattern(query))
    sql += " ORDER BY created_at DESC, id DESC"
    return _all(conn, sql, tuple(params))


def get_ticket(conn: sqlite3.Connection, ticket_id: int) -> dict | None:
    return _one(conn, f"SELECT {_TICKET_COLUMNS} FROM tickets WHERE id = ?", (ticket_id,))


def insert_ticket(conn: sqlite3.Connection, data: dict) -> int:
    cur = conn.execute(
        """
        INSERT INTO tickets (
            subject, body, created_at, search_blob, content_hash,
            ai_status, ai_category_code, ai_reasoning, ai_model
        ) VALUES (?, ?, ?, ?, ?, 'oczekuje', NULL, '', '')
        """,
        _values(data),
    )
    return int(cur.lastrowid)


def update_ticket(conn: sqlite3.Connection, ticket_id: int, data: dict) -> None:
    conn.execute(
        """
        UPDATE tickets SET
            subject = ?, body = ?, created_at = ?, search_blob = ?, content_hash = ?,
            ai_status = 'oczekuje', ai_category_code = NULL, ai_reasoning = '', ai_model = ''
        WHERE id = ?
        """,
        (*_values(data), ticket_id),
    )


def delete_ticket(conn: sqlite3.Connection, ticket_id: int) -> None:
    conn.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))


def count_tickets(conn: sqlite3.Connection) -> int:
    return int(conn.execute("SELECT COUNT(*) AS c FROM tickets").fetchone()["c"])


def clear_matches(conn: sqlite3.Connection) -> int:
    cur = conn.execute(
        """
        UPDATE tickets
        SET ai_status = 'oczekuje', ai_category_code = NULL, ai_reasoning = '', ai_model = ''
        """
    )
    return int(cur.rowcount)


def list_categories(conn: sqlite3.Connection) -> list[dict]:
    return _all(
        conn,
        "SELECT id, code, name, description, sort_order FROM categories ORDER BY sort_order, id",
    )


def get_category(conn: sqlite3.Connection, category_id: int) -> dict | None:
    return _one(conn, "SELECT id, code, name, description FROM categories WHERE id = ?", (category_id,))


def category_names(conn: sqlite3.Connection) -> dict[str, str]:
    return {row["code"]: row["name"] for row in list_categories(conn)}


def next_sort_order(conn: sqlite3.Connection) -> int:
    row = conn.execute("SELECT COALESCE(MAX(sort_order), 0) + 1 AS n FROM categories").fetchone()
    return int(row["n"])


def code_taken(conn: sqlite3.Connection, code: str) -> bool:
    return conn.execute("SELECT 1 FROM categories WHERE code = ?", (code,)).fetchone() is not None


def insert_category(conn: sqlite3.Connection, data: dict) -> int:
    cur = conn.execute(
        """
        INSERT INTO categories (code, name, description, sort_order)
        VALUES (?, ?, ?, ?)
        """,
        (data["code"], data["name"], data["description"], next_sort_order(conn)),
    )
    return int(cur.lastrowid)


def delete_category(conn: sqlite3.Connection, category_id: int) -> int | None:
    row = get_category(conn, category_id)
    if not row:
        return None
    cleared = conn.execute(
        """
        UPDATE tickets
        SET ai_status = 'oczekuje', ai_category_code = NULL, ai_reasoning = '', ai_model = ''
        WHERE ai_category_code = ?
        """,
        (row["code"],),
    ).rowcount
    conn.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    return int(cleared)
    return int(conn.execute("SELECT COUNT(*) AS c FROM tickets").fetchone()["c"])


def match_counts(conn: sqlite3.Connection) -> dict:
    row = conn.execute(
        """
        SELECT
            SUM(ai_status = 'oczekuje') AS oczekuje,
            SUM(ai_status = 'dopasowane') AS dopasowane,
            SUM(ai_status = 'brak') AS brak,
            SUM(ai_status = 'blad') AS blad,
            COUNT(*) AS total
        FROM tickets
        """
    ).fetchone()
    return {key: int(row[key] or 0) for key in ("oczekuje", "dopasowane", "brak", "blad", "total")}


def next_unmatched(conn: sqlite3.Connection, skip_ids: set[int]) -> dict | None:
    if skip_ids:
        marks = ",".join("?" for _ in skip_ids)
        sql = f"""
            SELECT id, subject, body, content_hash
            FROM tickets
            WHERE ai_status = 'oczekuje' AND id NOT IN ({marks})
            ORDER BY id
            LIMIT 1
        """
        params: tuple = tuple(skip_ids)
    else:
        sql = """
            SELECT id, subject, body, content_hash
            FROM tickets
            WHERE ai_status = 'oczekuje'
            ORDER BY id
            LIMIT 1
        """
        params = ()
    return _one(conn, sql, params)


def save_match(
    conn: sqlite3.Connection,
    ticket_id: int,
    expected_hash: str,
    *,
    status: str,
    category_code: str | None,
    reasoning: str,
    model: str,
) -> bool:
    cur = conn.execute(
        """
        UPDATE tickets
        SET ai_status = ?, ai_category_code = ?, ai_reasoning = ?, ai_model = ?
        WHERE id = ? AND content_hash = ? AND ai_status = 'oczekuje'
        """,
        (status, category_code, reasoning, model, ticket_id, expected_hash),
    )
    return cur.rowcount == 1


def _values(data: dict) -> tuple:
    subject = data["subject"]
    body = data["body"]
    return (
        subject,
        body,
        data["created_at"],
        search_blob(subject, body),
        content_hash(subject, body),
    )
