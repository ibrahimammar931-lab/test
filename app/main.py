from fastapi import FastAPI

from .database import Base, engine
from .routes import authors, books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API")

app.include_router(authors.router)
app.include_router(books.router)


@app.get("/")
def root():
    return {"message": "Bookstore API"}