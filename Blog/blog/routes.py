from fastapi import APIRouter, Depends, status, Response, HTTPException
from . import models, schemas
from .database import get_db
from .schemas import BlogCreate, BlogUpdate, ShowBlog
from sqlalchemy.orm import Session


blog_route = APIRouter(prefix="/blogs", tags=["Blogs"])


@blog_route.get( "/", response_model=list[ShowBlog], status_code=status.HTTP_200_OK)
async def read_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@blog_route.get("/{blog_id}", status_code=status.HTTP_200_OK)
async def read_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog


@blog_route.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED )
async def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(**blog.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@blog_route.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@blog_route.put("/{blog_id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
async def update_blog(blog_id: int, updated_blog: BlogUpdate, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    for key, value in updated_blog.model_dump().items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return blog