from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.book import BookCreate, BookUpdate, ShowBook
from app.core.database import engine, Base, get_db
from sqlalchemy.orm import Session

from app.services import book_services


book_router = APIRouter()

Base.metadata.create_all(bind=engine) # Create the tables in the database


@book_router.get("/books")
async def get_books(db: Session = Depends(get_db)):
    return book_services.get_all_books(db)


@book_router.post("/books")
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_services.create_book(db, book)


@book_router.get("/books/{book_id}")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return book_services.get_book(db, book_id)


@book_router.put("/books/{book_id}")
async def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    return book_services.update_book(db, book_id, book)


@book_router.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    return book_services.delete_book(db, book_id)