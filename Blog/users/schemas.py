from pydantic import BaseModel, ConfigDict
from typing import List


class User(BaseModel):
    name: str
    email: str
    password: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ShowUser(BaseModel):
    name: str
    email: str
    # fully-qualified forward reference to avoid importing blog.schemas at runtime
    blogs: List["blog.schemas.Blog"] = []

    model_config = ConfigDict(from_attributes=True)


class UserCreate(User):
    pass