from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import SessionLocal
from ..auth import require_roles

router = APIRouter(prefix="/books", tags=["Books"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.BookOut, dependencies=[Depends(require_roles("Admin", "Editor"))])
def create(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@router.get("/", response_model=list[schemas.BookOut], dependencies=[Depends(require_roles("Admin", "Editor", "Viewer"))])
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookOut, dependencies=[Depends(require_roles("Admin", "Editor", "Viewer"))])
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book


@router.put("/{book_id}", response_model=schemas.BookOut, dependencies=[Depends(require_roles("Admin", "Editor"))])
def update(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(404, "Book not found")
    return updated


@router.delete("/{book_id}", dependencies=[Depends(require_roles("Admin"))])
def delete(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(404, "Book not found")
    return {"message": "Deleted"}
