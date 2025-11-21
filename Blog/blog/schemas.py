from pydantic import BaseModel

class Blog(BaseModel):
    id: int
    title: str
    content: str
    published: bool | None = True