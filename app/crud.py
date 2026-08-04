from sqlalchemy.orm import Session

from . import models, schemas


# --- Authors ---
def create_author(db: Session, author: schemas.AuthorCreate) -> models.Author:
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_authors(db: Session) -> list[models.Author]:
    return db.query(models.Author).all()


def get_author(db: Session, author_id: int) -> models.Author | None:
    return db.query(models.Author).filter(models.Author.id == author_id).first()


# --- Books ---
def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session) -> list[models.Book]:
    return db.query(models.Book).all()


def get_book(db: Session, book_id: int) -> models.Book | None:
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def update_book(db: Session, book_id: int, book: schemas.BookUpdate) -> models.Book | None:
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    for field, value in book.model_dump(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    db_book = get_book(db, book_id)
    if not db_book:
        return False
    db.delete(db_book)
    db.commit()
    return True


# --- Audit Logs ---
def create_audit_log(db: Session, audit_data: dict) -> models.AuditLog:
    db_audit = models.AuditLog(**audit_data)
    db.add(db_audit)
    db.commit()
    db.refresh(db_audit)
    return db_audit


def get_audit_logs(db: Session) -> list[models.AuditLog]:
    return db.query(models.AuditLog).order_by(models.AuditLog.created_at.desc()).all()
