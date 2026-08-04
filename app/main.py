from fastapi import FastAPI

from .audit import AuditLogMiddleware
from .database import Base, engine
from .routes import audit_logs, authors, books

# Ensure all models are registered before creating tables
from . import models  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API")

app.add_middleware(AuditLogMiddleware)

app.include_router(authors.router)
app.include_router(books.router)
app.include_router(audit_logs.router)


@app.get("/")
def root():
    return {"message": "Bookstore API"}
