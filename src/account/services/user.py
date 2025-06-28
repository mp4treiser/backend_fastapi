from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.account.repositories.user import UserRepository
from src.account.schemas import CreateUserSchema, UserListSchema, UpdateUserSchema


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = UserRepository(session=session)

    def create(self, user_schema: CreateUserSchema):
        self._validate_email_unique(email=user_schema.email)
        self._validate_role_exists(role_id=user_schema.role_id)
        return self.repository.create(user_schema=user_schema)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id=user_id)

    def update(self, user_id: int, user_schema: UpdateUserSchema):
        return self.repository.update(user_id=user_id, user_schema=user_schema)

    def delete(self, user_id: int):
        try:
            return self.repository.delete(user_id=user_id)
        except NoResultFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

    def _validate_email_unique(self, email: str):
        return self.repository.check_email(email=email)

    def _validate_role_exists(self, role_id: int):
        return self.repository.check_role(role_id=role_id)