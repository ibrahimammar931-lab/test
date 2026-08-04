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

## API Key

Write endpoints (POST, PUT, DELETE) require an API key sent in the `X-API-Key` header.

- Set the expected key via the `BOOKSTORE_API_KEY` environment variable (e.g., `export BOOKSTORE_API_KEY=your-secret-key`).
- If the variable is not set, the default key is `change-me` (for development only).
- Requests missing the header or with an incorrect key will receive a `401 Unauthorized` response.
