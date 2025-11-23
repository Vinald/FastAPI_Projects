
from pydantic import BaseModel
from typing import List
from ..blog.schemas import Blog


class User(BaseModel):
    name: str
    email: str
    password: str | None = None

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class UserCreate(User):
    pass