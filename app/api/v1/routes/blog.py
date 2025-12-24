from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.core.database import get_db
from app.schemas.blog import BlogCreate, BlogUpdate, ShowBlog
from sqlalchemy.orm import Session
from app.services import blog_services


blog_route = APIRouter(prefix="/blogs", tags=["Blogs"])


# create a blog
@blog_route.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED )
async def create_blog(blog_data: BlogCreate, db: Session = Depends(get_db)):
    return blog_services.create(blog_data, db)


# get all blogs
@blog_route.get( "/", response_model=list[ShowBlog], status_code=status.HTTP_200_OK)
async def read_blogs(db: Session = Depends(get_db)):
    return blog_services.get_all(db)


# get a blog by id
@blog_route.get("/{blog_id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
async def read_blog(blog_id: int, db: Session = Depends(get_db)):
    return blog_services.get_by_id(blog_id, db)


# update a blog
@blog_route.put("/{blog_id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
async def update_blog(blog_id: int, updated_blog: BlogUpdate, db: Session = Depends(get_db)):
    return blog_services.update(blog_id, updated_blog, db)


# delete a blog
@blog_route.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    return blog_services.destroy(blog_id, db)
