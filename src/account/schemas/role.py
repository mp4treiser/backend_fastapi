from pydantic import BaseModel


class BaseRoleSchema(BaseModel):
    name: str

class RoleCreateSchema(BaseRoleSchema):
    pass


class RoleUpdateSchema(BaseRoleSchema):
    pass


class RoleReadSchema(BaseRoleSchema):
    id: int

class RoleListSchema(BaseRoleSchema):
    id: int