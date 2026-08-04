# Bookstore API

Simple FastAPI application for managing authors and books.

## Structure
- `app/main.py` — application entrypoint, registers routers
- `app/database.py` — SQLite + SQLAlchemy setup
- `app/models.py` — ORM models (Author, Book)
- `app/schemas.py` — Pydantic request/response schemas
- `app/crud.py` — database operations
- `app/routes/authors.py` — author endpoints
- `app/routes/books.py` — book endpoints

## Run
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```