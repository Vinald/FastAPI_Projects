from typing import List
from fastapi import FastAPI, HTTPException, Depends
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from schema import BookCreate, BookRead, BookUpdate

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






def book_to_dict(b):
    return {
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "description": b.description,
        "rating": b.rating,
    }


@app.get("/books", response_model=List[BookRead])
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()

@app.get("/books/{book_id}", response_model=BookRead)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    b = db.query(models.Books).filter(models.Books.id == book_id).first()
    if not b:
        raise HTTPException(status_code=404, detail="Book not found")
    return b

@app.post("/books", response_model=BookRead, status_code=201)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_model = models.Books(**book.model_dump())
    db.add(book_model)
    db.commit()
    db.refresh(book_model)
    return book_model


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if not book_model:
        raise HTTPException(status_code=404, detail="Book not found")
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating
    db.commit()
    return {"message": "Book Updated"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if not book_model:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book_model)
    db.commit()
    return {"message": "Book Deleted"}
