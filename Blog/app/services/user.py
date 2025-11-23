from ..users.models import User as UserModel
from sqlalchemy.orm import Session
from ..users.schemas import UserCreate, UserUpdate
from fastapi import HTTPException, status
from ..users.hashing import Hash


def get_all(db: Session):
    return db.query(UserModel).all()


def create(user_date: UserCreate, db: Session):
    hashed_password = Hash.bcrypt(user_date.password)
    new_user = UserModel(name=user_date.name, email=user_date.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_by_id(user_id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {UserModel.id} not found")
    return user


def update(user_id: int, updated_data: UserUpdate, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    for key, value in updated_data.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


def destroy(user_id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return
