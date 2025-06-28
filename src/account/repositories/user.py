from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.account.schemas import CreateUserSchema, UpdateUserSchema, UserListSchema
from src.account.models import User, Role
from sqlalchemy import Select, Update, Delete


class UserRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    def create(self, user_schema: CreateUserSchema):
        user = User(
            first_name = user_schema.first_name,
            last_name = user_schema.last_name,
            email = user_schema.email,
            role_id = user_schema.role_id
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self, user_id: int, user_schema: UpdateUserSchema):
        user_dict = user_schema.dict(exclude_unset=True)
        query = Update(User).where(User.id == user_id).values(**user_dict)
        self.session.execute(query)
        self.session.commit()
        updated_user = self.session.get(User, user_id)
        return updated_user

    def delete(self, user_id: int):
        query = Delete(User).where(User.id == user_id)
        result = self.session.execute(query)
        if result.rowcount == 0:
            raise NoResultFound(f"User with id {user_id} not found")
        self.session.commit()
        return {"detail": "success"}

    def get_by_id(self, user_id: int):
        user = self.session.get(User, user_id)
        return user

    def get_all(self):
        query = Select(User)
        result = self.session.execute(query)
        users = result.scalars().all()
        return users

    def check_email(self, email):
        query = Select(User).where(User.email == email)
        result = self.session.execute(query)
        if result.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    def check_role(self, role_id):
        query = Select(Role).where(Role.id == role_id)
        result = self.session.execute(query)
        if result.scalar_one_or_none() is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Role with {role_id} is not found"
            )


