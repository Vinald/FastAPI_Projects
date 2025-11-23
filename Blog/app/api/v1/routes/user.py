from fastapi import APIRouter, Depends, status
from Blog.users.schemas import ShowUser, UserCreate
from Blog.database import get_db
from sqlalchemy.orm import Session
from ..repository import user as user_repository

user_route = APIRouter(prefix="/users", tags=["Users"])


@user_route.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user_repository.create(user_data, db)


@user_route.get("/", response_model=list[ShowUser])
async def read_users(db: Session = Depends(get_db)):
    return user_repository.get_all(db)


@user_route.get("/{user_id}", response_model=ShowUser)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return user_repository.get_by_id(user_id, db)


@user_route.put("/{user_id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, updated_user: ShowUser, db: Session =
Depends(get_db)):
    return user_repository.update(user_id, updated_user, db)


@user_route.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_repository.destroy(user_id, db)
