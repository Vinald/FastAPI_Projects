from __future__ import annotations
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

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
