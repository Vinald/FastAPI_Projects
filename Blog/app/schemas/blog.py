from pydantic import BaseModel
from user import ShowUser


class BlogBase(BaseModel):
    title: str
    content: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class ShowBlog(BlogBase):
    creator: ShowUser

    class Config:
        orm_mode = True


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogInDB(BlogBase):
    id: int

    class Config:
        orm_mode = True
