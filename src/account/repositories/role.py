from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.account.schemas import RoleUpdateSchema, RoleReadSchema, RoleCreateSchema
from src.account.models.role import Role
from sqlalchemy import Select, Update, Delete


class RoleRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    def create(self, role_schema: RoleCreateSchema):
        role = Role(
            name = role_schema.name
        )
        self.session.add(role)
        self.session.commit()
        self.session.refresh(role)
        return role

    def update(self, role_id: int, role_schema: RoleUpdateSchema):
        role_dict = role_schema.dict()
        query = Update(Role).where(Role.id == role_id).values(**role_dict)
        self.session.execute(query)
        self.session.commit()
        updated_role = self.session.get(Role, role_id)
        return updated_role

    def delete(self, role_id: int):
        query = Delete(Role).where(Role.id == role_id)
        result = self.session.execute(query)
        if result.rowcount == 0:
            raise NoResultFound(f"Role with id {role_id} not found")
        self.session.commit()
        return {"detail": "success"}

    def get_by_id(self, role_id: int):
        role = self.session.get(Role, role_id)
        return role

    def get_all(self):
        query = Select(Role)
        result = self.session.execute(query)
        roles = result.scalars().all()
        return roles