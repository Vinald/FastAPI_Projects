from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str | None = None

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserCreate(User):
    pass