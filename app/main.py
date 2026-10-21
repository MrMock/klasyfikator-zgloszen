"""Prosty panel zgłoszeń i odczyt JSON."""

import sqlite3
from contextlib import asynccontextmanager
from urllib.parse import urlencode

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import db, repo, seed
from app.classifier import worker
from app.forms import (
    blank_category_form,
    blank_ticket_form,
    parse_category,
    parse_ticket,
    posted_category,
    posted_ticket,
    ticket_to_form,
)
from app.textutil import format_dt, format_dt_long, preview

APP_DIR = db.ROOT / "app"
templates = Jinja2Templates(directory=str(APP_DIR / "templates"))
templates.env.filters["dt"] = format_dt
templates.env.filters["dt_long"] = format_dt_long
templates.env.filters["preview"] = preview

OK_MESSAGES = {
    "zapisano": "Zapisano zgłoszenie.",
    "usunieto": "Usunięto zgłoszenie.",
    "wyczyszczono": "Wyczyszczono dopasowania. Model liczy od nowa.",
    "dodano": "Dodano kategorię.",
    "usunieto_kategorie": "Usunięto kategorię. Zgłoszenia z niej wróciły do liczenia.",
}

PAGE_SIZE = 20


@asynccontextmanager
async def lifespan(_app: FastAPI):
    db.init()
    if seed.seed_if_empty():
        print("Wczytano przykładowe dane: 100 zgłoszeń.")
    worker.start()
    yield
    worker.stop()


app = FastAPI(title="Zgłoszenia helpdesku", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")


def get_db():
    conn = db.connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def _page(request: Request, name: str, context: dict, status_code: int = 200, nav: str = ""):
    context["nav"] = nav
    context["flash"] = OK_MESSAGES.get(request.query_params.get("ok", ""), "")
    return templates.TemplateResponse(
        request=request, name=name, context=context, status_code=status_code
    )


def _redirect(url: str) -> RedirectResponse:
    return RedirectResponse(url, status_code=303)


@app.exception_handler(HTTPException)
async def handle_http(request: Request, exc: HTTPException):
    if request.url.path.startswith("/api"):
        return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)
    return _page(
        request,
        "error.html",
        {"message": exc.detail, "status_code": exc.status_code},
        status_code=exc.status_code,
    )


@app.get("/")
def tickets_page(request: Request, conn: sqlite3.Connection = Depends(get_db)):
    query = request.query_params.get("q", "").strip()
    rows = repo.list_tickets(conn, query)
    try:
        page = int(request.query_params.get("page", "1"))
    except ValueError:
        page = 1
    total = len(rows)
    pages = max(1, (total + PAGE_SIZE - 1) // PAGE_SIZE)
    page = min(max(page, 1), pages)
    start = (page - 1) * PAGE_SIZE
    return _page(
        request,
        "tickets.html",
        {
            "query": query,
            "tickets": rows[start : start + PAGE_SIZE],
            "total": total,
            "page": page,
            "pages": pages,
            "counts": repo.match_counts(conn),
            "category_names": repo.category_names(conn),
            "page_href": lambda number: _page_href(query, number),
        },
        nav="zgloszenia",
    )


@app.get("/zgloszenia/nowe")
def new_ticket_form(request: Request):
    return _ticket_form(request, blank_ticket_form(), "", None)


@app.post("/zgloszenia")
def create_ticket(
    request: Request,
    subject: str = Form(""),
    body: str = Form(""),
    created_at: str = Form(""),
    conn: sqlite3.Connection = Depends(get_db),
):
    raw = {"subject": subject, "body": body, "created_at": created_at}
    data, error = parse_ticket(raw)
    if error:
        return _ticket_form(request, posted_ticket(raw), error, None, 400)
    ticket_id = repo.insert_ticket(conn, data)
    conn.commit()
    worker.kick()
    return _redirect(f"/zgloszenia/{ticket_id}?ok=zapisano")


@app.get("/zgloszenia/{ticket_id}")
def ticket_detail(request: Request, ticket_id: int, conn: sqlite3.Connection = Depends(get_db)):
    ticket = repo.get_ticket(conn, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Nie ma takiego zgłoszenia.")
    return _page(
        request,
        "ticket_detail.html",
        {"ticket": ticket, "category_names": repo.category_names(conn)},
        nav="zgloszenia",
    )


@app.get("/zgloszenia/{ticket_id}/edytuj")
def edit_ticket_form(request: Request, ticket_id: int, conn: sqlite3.Connection = Depends(get_db)):
    ticket = repo.get_ticket(conn, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Nie ma takiego zgłoszenia.")
    return _ticket_form(request, ticket_to_form(ticket), "", ticket_id)


@app.post("/zgloszenia/{ticket_id}")
def update_ticket(
    request: Request,
    ticket_id: int,
    subject: str = Form(""),
    body: str = Form(""),
    created_at: str = Form(""),
    conn: sqlite3.Connection = Depends(get_db),
):
    if not repo.get_ticket(conn, ticket_id):
        raise HTTPException(status_code=404, detail="Nie ma takiego zgłoszenia.")
    raw = {"subject": subject, "body": body, "created_at": created_at}
    data, error = parse_ticket(raw)
    if error:
        return _ticket_form(request, posted_ticket(raw), error, ticket_id, 400)
    repo.update_ticket(conn, ticket_id, data)
    conn.commit()
    worker.kick()
    return _redirect(f"/zgloszenia/{ticket_id}?ok=zapisano")


@app.post("/zgloszenia/{ticket_id}/usun")
def remove_ticket(ticket_id: int, conn: sqlite3.Connection = Depends(get_db)):
    repo.delete_ticket(conn, ticket_id)
    return _redirect("/?ok=usunieto")


@app.get("/kategorie/nowa")
def new_category_form(request: Request):
    return _category_form(request, blank_category_form(), "")


@app.post("/kategorie")
def create_category(
    request: Request,
    name: str = Form(""),
    code: str = Form(""),
    description: str = Form(""),
    conn: sqlite3.Connection = Depends(get_db),
):
    raw = {"name": name, "code": code, "description": description}
    data, error = parse_category(raw)
    if error:
        return _category_form(request, posted_category(raw), error, 400)
    typed_code = str(code or "").strip()
    if typed_code and repo.code_taken(conn, data["code"]):
        return _category_form(request, posted_category(raw), "Ten kod jest już zajęty.", 400)
    if not typed_code:
        data["code"] = _free_code(conn, data["code"])
    try:
        repo.insert_category(conn, data)
    except sqlite3.IntegrityError:
        return _category_form(request, posted_category(raw), "Taka kategoria już istnieje.", 400)
    return _redirect("/kategorie?ok=dodano")


@app.post("/kategorie/{category_id}/usun")
def remove_category(category_id: int, conn: sqlite3.Connection = Depends(get_db)):
    cleared = repo.delete_category(conn, category_id)
    if cleared is None:
        raise HTTPException(status_code=404, detail="Nie ma takiej kategorii.")
    if cleared:
        conn.commit()
        worker.kick()
    return _redirect("/kategorie?ok=usunieto_kategorie")


@app.get("/kategorie")
def categories_page(request: Request, conn: sqlite3.Connection = Depends(get_db)):
    return _page(
        request,
        "categories.html",
        {"labels": repo.list_categories(conn), "counts": repo.match_counts(conn)},
        nav="kategorie",
    )


@app.post("/kategorie/wyczysc")
def clear_categories(conn: sqlite3.Connection = Depends(get_db)):
    repo.clear_matches(conn)
    conn.commit()
    worker.kick()
    return _redirect("/kategorie?ok=wyczyszczono")


@app.get("/api/zgloszenia")
def api_tickets(conn: sqlite3.Connection = Depends(get_db)):
    names = repo.category_names(conn)
    return [_public_ticket(row, names) for row in repo.list_tickets(conn)]


@app.get("/api/zgloszenia/{ticket_id}")
def api_ticket(ticket_id: int, conn: sqlite3.Connection = Depends(get_db)):
    row = repo.get_ticket(conn, ticket_id)
    if not row:
        raise HTTPException(status_code=404, detail="Nie ma takiego zgłoszenia.")
    return _public_ticket(row, repo.category_names(conn))


def _ticket_form(request, form, error, ticket_id, status_code: int = 200):
    return _page(
        request,
        "ticket_form.html",
        {"form": form, "form_error": error, "ticket_id": ticket_id},
        status_code=status_code,
        nav="zgloszenia",
    )


def _category_form(request, form, error, status_code: int = 200):
    return _page(
        request,
        "category_form.html",
        {"form": form, "form_error": error},
        status_code=status_code,
        nav="kategorie",
    )


def _free_code(conn, code: str) -> str:
    candidate = code
    number = 2
    while repo.code_taken(conn, candidate):
        suffix = f"-{number}"
        candidate = f"{code[: 48 - len(suffix)]}{suffix}"
        number += 1
    return candidate


def _public_ticket(row: dict, names: dict[str, str]) -> dict:
    code = row["ai_category_code"] if row["ai_status"] == "dopasowane" else None
    return {
        "id": row["id"],
        "subject": row["subject"],
        "body": row["body"],
        "created_at": row["created_at"],
        "ai_status": row["ai_status"],
        "ai_category": names.get(code, code) if code else None,
        "ai_reasoning": row["ai_reasoning"],
        "ai_model": row["ai_model"],
    }


def _page_href(query: str, page: int) -> str:
    data = {"page": str(page)}
    if query:
        data["q"] = query
    return "/?" + urlencode(data)
