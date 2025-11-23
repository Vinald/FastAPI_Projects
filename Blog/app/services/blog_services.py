from ..models.blog import Blog as BlogModel
from sqlalchemy.orm import Session
from ..schemas.blog import BlogCreate, BlogUpdate
from fastapi import  HTTPException, status


def get_all(db: Session):
    return db.query(BlogModel).all()


def create(blog_data: BlogCreate, db: Session):
    new_blog = BlogModel(**blog_data.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_by_id(blog_id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {BlogModel.id} not found")
    return blog


def update(blog_id: int, updated_data: BlogUpdate, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {BlogModel.id} not found")
    for key, value in updated_data.items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return blog


def destroy(blog_id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {BlogModel.id} not found")
    db.delete(blog)
    db.commit()
    return