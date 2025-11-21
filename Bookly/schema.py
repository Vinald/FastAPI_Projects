from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    rating: int


class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True


class BookUpdate(BookRead):
    pass