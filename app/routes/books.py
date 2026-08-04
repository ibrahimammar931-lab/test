from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.BookOut)
def create(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@router.get("/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book

@router.put("/{book_id}", response_model=schemas.BookOut)
def update(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if not updated:
        raise HTTPException(404, "Book not found")
    return updated

@router.delete("/{book_id}")
def delete(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(404, "Book not found")
    return {"message": "Deleted"}