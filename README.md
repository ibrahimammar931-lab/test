# Bookstore API

Simple FastAPI application for managing authors and books.

## Structure
- `app/main.py` — application entrypoint, registers routers
- `app/database.py` — SQLite + SQLAlchemy setup
- `app/models.py` — ORM models (Author, Book)
- `app/schemas.py` — Pydantic request/response schemas
- `app/crud.py` — database operations
- `app/auth.py` — role-based access control dependency
- `app/routes/authors.py` — author endpoints
- `app/routes/books.py` — book endpoints

## Authentication and Authorization

Role-based access control is implemented via the `X-Role` HTTP header.

| Role   | Permissions                                                                 |
|--------|-----------------------------------------------------------------------------|
| Admin  | Full CRUD on authors and books                                              |
| Editor | Create and update books; cannot delete books or access author endpoints    |
| Viewer | Read-only access to authors and books (GET requests only)                  |

Missing or invalid `X-Role` returns `403 Forbidden`.

## Run
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
