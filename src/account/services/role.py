from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.account.repositories.role import RoleRepository
from src.account.schemas import RoleCreateSchema, RoleUpdateSchema, RoleReadSchema


class RoleService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = RoleRepository(session=session)

    def create(self, role_schema: RoleCreateSchema):
        return self.repository.create(role_schema=role_schema)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, role_id: int):
        return self.repository.get_by_id(role_id=role_id)

    def update(self, role_id: int, role_schema: RoleUpdateSchema):
        return self.repository.update(role_id=role_id, role_schema=role_schema)

    def delete(self, role_id: int):
        try:
            return self.repository.delete(role_id=role_id)
        except NoResultFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Role with id {role_id} not found"
            )