from fastapi import FastAPI
from .api.v1.routes import book, user

app = FastAPI()

version = "v1"

app.include_router(book.book_router, prefix=f"/api/{version}")



