from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import SessionLocal
from ..security import require_api_key

router = APIRouter(prefix="/books/{book_id}/reviews", tags=["reviews"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=list[schemas.ReviewOut])
def list_reviews(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.get_reviews_for_book(db, book_id)


@router.post("", response_model=schemas.ReviewOut, dependencies=[Depends(require_api_key)])
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.create_review(db, book_id, review)
