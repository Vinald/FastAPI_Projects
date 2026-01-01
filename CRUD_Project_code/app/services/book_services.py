from fastapi import HTTPException, status
from app.models.book import Book as BookModel
from app.schemas.book import BookCreate, BookUpdate, ShowBook
from sqlalchemy.orm import Session


def create_book(db: Session, book: BookCreate):
    db_book = BookModel(title=book.title, author=book.author, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BookModel).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    if not book_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book {book_id} not found")
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book {book_id} not found")

    db_book.title = book.title
    db_book.author = book.author
    db_book.description = book.description
    db.commit()
    db.refresh(db_book)

    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book {book_id} not found")

    db.delete(db_book)
    db.commit()
    return db_book