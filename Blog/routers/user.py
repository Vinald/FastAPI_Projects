from fastapi import APIRouter, Depends, HTTPException, status
from Blog.users.schemas import ShowUser, UserCreate
from Blog.database import get_db
from sqlalchemy.orm import Session
from ..users.models import User
from ..users.hashing import Hash


user_route = APIRouter(prefix="/users", tags=["Users"])

@user_route.get("/", response_model=list[ShowUser])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@user_route.get("/{user_id}", response_model=ShowUser)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    return user


@user_route.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return


@user_route.put("/{user_id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, updated_user: ShowUser, db: Session =
Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    for key, value in updated_user.model_dump().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@user_route.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
