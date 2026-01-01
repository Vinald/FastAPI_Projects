from pydantic import BaseModel, Field
from uuid import UUID


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=200)


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class ShowBook(BookBase):
    pass