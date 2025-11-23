from __future__ import annotations
from typing import List
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    email: str
    password: str | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List["Blog"] = []

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


# ⭐ REQUIRED FOR Pydantic v2
ShowUser.model_rebuild()
