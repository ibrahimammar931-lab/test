from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import SessionLocal
from ..auth import require_roles

router = APIRouter(prefix="/authors", tags=["Authors"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.AuthorOut, dependencies=[Depends(require_roles("Admin"))])
def create(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)


@router.get("/", response_model=list[schemas.AuthorOut], dependencies=[Depends(require_roles("Admin", "Viewer"))])
def list_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)


@router.get("/{author_id}", response_model=schemas.AuthorOut, dependencies=[Depends(require_roles("Admin", "Viewer"))])
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if not author:
        raise HTTPException(404, "Author not found")
    return author
