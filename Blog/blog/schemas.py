from pydantic import BaseModel, ConfigDict


class BlogBase(BaseModel):
    title: str
    content: str


class Blog(BlogBase):
    # allow creation from SQLAlchemy objects
    model_config = ConfigDict(from_attributes=True)


class ShowBlog(BlogBase):
    # use a fully-qualified forward reference to avoid a runtime import and circular import
    creator: "users.schemas.ShowUser"

    model_config = ConfigDict(from_attributes=True)


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogInDB(BlogBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

