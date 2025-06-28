from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.schemas import RoleCreateSchema, RoleReadSchema, RoleUpdateSchema, RoleListSchema
from src.account.services.role import RoleService
#from src.core.orm import create_tables
from src.core.orm.database import get_sync_session

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

@router.get("/health")
def health_handler():
    return {"work": "success"}

@router.get("/", response_model=List[RoleListSchema])
def get_roles_handler(session: AsyncSession = Depends(get_sync_session)):
    roles = RoleService(session=session)
    return roles.get_all()

@router.get("/{role_id}", response_model=RoleReadSchema)
def get_role_by_id_handler(role_id: int, session: AsyncSession = Depends(get_sync_session)):
    roles = RoleService(session=session)
    return roles.get_by_id(role_id=role_id)

@router.post("/", response_model=RoleListSchema)
def create_role_handler(payload: RoleCreateSchema, session: AsyncSession = Depends(get_sync_session)):
    role_service = RoleService(session=session)
    return role_service.create(role_schema=payload)

@router.put("/{role_id}", response_model=RoleListSchema)
def update_role_handler(role_id: int, payload: RoleUpdateSchema, session: AsyncSession = Depends(get_sync_session)):
    role_service = RoleService(session=session)
    return role_service.update(role_id=role_id, role_schema=payload)

@router.delete("/{role_id}", response_model=None)
def delete_role_handler(role_id: int, session: AsyncSession = Depends(get_sync_session)):
    role_service = RoleService(session=session)
    return role_service.delete(role_id=role_id)