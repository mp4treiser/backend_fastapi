from pydantic import BaseModel
from typing import Optional

class BaseUserSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    role_id: int

class UpdateUserSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role_id: Optional[int] = None

class CreateUserSchema(BaseUserSchema):
    pass

class UserListSchema(BaseUserSchema):
    id: int
    is_superuser: bool | None = None
    is_active: bool | None = None

class UserReadSchema(BaseUserSchema):
    id: int
    is_superuser: bool | None = None
    is_active: bool | None = None
