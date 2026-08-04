from sqlalchemy.orm import Session

from . import models, schemas


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


def create_review(db: Session, book_id: int, review: schemas.ReviewCreate) -> models.Review:
    db_review = models.Review(book_id=book_id, **review.model_dump())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews_for_book(db: Session, book_id: int) -> list[models.Review]:
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()
