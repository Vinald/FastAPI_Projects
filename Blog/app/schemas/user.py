
from pydantic import BaseModel
from typing import List
from blog import Blog


class UserBase(BaseModel):
    name: str
    email: str
    password: str | None = None


class User(UserBase):
    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass