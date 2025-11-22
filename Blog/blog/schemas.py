from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    content: str


class ShowBlog(Blog):
    class Config:
        orm_mode = True


class BlogCreate(Blog):
    pass


class BlogUpdate(Blog):
    pass


class BlogInDB(Blog):
    id: int

    class Config:
        orm_mode = True
