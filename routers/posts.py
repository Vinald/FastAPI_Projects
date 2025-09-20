from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


post_router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

my_posts = [{"id": 1, "title": "Post 1", "content": "Content of post 1", "published": True, "rating": 5},
            {"id": 2, "title": "Post 2", "content": "Content of post 2",  "published": False, "rating": None}]


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


def find_post(post_id: int):
    for post in my_posts:
        if post["id"] == post_id:
            return post
    return None


@post_router.get("/")
async def get_posts():
    return {"posts": my_posts}


@post_router.post("/")
async def create_post(post: Post):
    new_post = post.model_dump()
    new_post["id"] = len(my_posts) + 1
    my_posts.append(new_post)
    return {"message": "Post created successfully", "post": new_post}


@post_router.get("/{post_id}")
async def get_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post not found {post_id}")
    return {"post": post}


@post_router.put("/{post_id}")
async def update_post(post_id: int, updated_post: Post):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post not found {post_id}")
    post.update(updated_post.model_dump())
    return {"message": "Post updated successfully", "post": post}


@post_router.delete("/{post_id}")
async def delete_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post not found {post_id}")
    my_posts.remove(post)
    return {"message": "Post deleted successfully"}
