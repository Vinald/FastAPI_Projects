from fastapi import APIRouter
from .schemas import Blog

blog_route = APIRouter(prefix="/blogs", tags=["Blogs"])


@blog_route.get("/")
async def read_root():
    return {"Hello": "World"}


@blog_route.get("/{blog_id}")
async def read_blog(blog_id: int):
    return {"blog_id": blog_id}


@blog_route.get("/{blog_id}/comments")
async def read_blog_comments(blog_id: int, limit: int = 10):
    return {"blog_id": blog_id, "comments_limit": limit}


@blog_route.get("/about")
async def about_page():
    return {"About": "This is a sample FastAPI application."}


@blog_route.post("/")
async def create_blog(blog: Blog):
    return {"message": "Blog created successfully", "blog": blog}