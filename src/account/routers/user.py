from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.schemas.user import users, UserListSchema, CreateUserSchema, UpdateUserSchema
from src.account.services.user import UserService
#from src.core.orm import create_tables
from src.core.orm.database import get_sync_session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/health")
def health_handler():
    return {"work": "success"}

@router.get("/", response_model=List[UserListSchema])
def get_users_handler(session: AsyncSession = Depends(get_sync_session)):
    users = UserService(session=session)
    return users.get_list()

@router.post("/", response_model=UserListSchema)
def create_user_handler(payload: CreateUserSchema, session: AsyncSession = Depends(get_sync_session)):
    user_service = UserService(session=session)
    return user_service.create(user_schema=payload)

@router.put("/{user_id}", response_model=UserListSchema)
def update_user_handler(user_id: int, payload: UpdateUserSchema):
    user = [user for user in users if user["id"]==user_id][0]
    user["first_name"] = payload.first_name
    user["last_name"] = payload.last_name
    return user

