from __future__ import annotations
from pydantic import BaseModel, ConfigDict


class BlogBase(BaseModel):
    title: str
    content: str


class Blog(BlogBase):
    id: int
    creator: "app.schemas.user.ShowUser" | None = None

    model_config = ConfigDict(from_attributes=True)


class ShowBlog(BlogBase):
    id: int
    creator: "app.schemas.user.ShowUser"

    model_config = ConfigDict(from_attributes=True)


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogInDB(BlogBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# ⭐ REQUIRED IN Pydantic v2
Blog.model_rebuild()
ShowBlog.model_rebuild()
