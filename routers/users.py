from typing import List

from fastapi import APIRouter, Depends, Query
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette import status

from dependency import get_db
from models.user import User
from schemas import UserSchema, UserCreate
import service.user as user_service
import service.image as image_service

router = APIRouter()


@router.post("/users", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    *,
    user: UserCreate = Depends(UserCreate.from_formdata),
    db: Session = Depends(get_db)
) -> UserSchema:
    image_path = await image_service.save_file(user.image)
    obj_data = jsonable_encoder(user)
    user_db = User(**obj_data, image_path=image_path)
    return user_service.create_user(db, user_db)


@router.get("/users", response_model=List[UserSchema])
def read_users(*, db: Session = Depends(get_db)):
    return user_service.get_users(db)

