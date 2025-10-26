from fastapi import APIRouter, HTTPException, status, Response
from typing import List, Optional
from .model import Post, PostOut
from .data import  POSTS

post_router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

def find_post(post_id: int) -> Optional[dict]:
    return next((post for post in POSTS if post["id"] == post_id), None)


def get_next_id() -> int:
    if POSTS:
        return max(post["id"] for post in POSTS) + 1
    return 1


@post_router.get("/", response_model=List[PostOut])
async def get_posts():
    return POSTS


@post_router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: Post):
    new_post = post.model_dump()
    new_post["id"] = get_next_id()
    POSTS.append(new_post)
    return new_post


@post_router.get("/{post_id}", response_model=PostOut)
async def get_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {post_id} not found")
    return post


@post_router.put("/{post_id}", response_model=PostOut)
async def update_post(post_id: int, updated_post: Post):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {post_id} not found")
    post.update(updated_post.model_dump())
    return post


@post_router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {post_id} not found")
    POSTS.remove(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
