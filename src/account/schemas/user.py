from pydantic import BaseModel

users = [
    {
        "id": 1,
        "email": "admin@admin.admin",
        "first_name": "admin@admin.admin",
        "last_name": "admin@admin.admin",
        "is_superuser": False,
    },
    {
        "id": 2,
        "email": "admin1@admin.admin",
        "first_name": "admin1@admin.admin",
        "last_name": "admin1@admin.admin",
        "is_superuser": False,
    },
    {
        "id": 3,
        "email": "admin2@admin.admin",
        "first_name": "admin2@admin.admin",
        "last_name": "admin2@admin.admin",
        "is_superuser": False,
    },
    {
        "id": 3,
        "email": "admin3@admin.admin",
        "first_name": "admin3@admin.admin",
        "last_name": "admin3@admin.admin",
        "is_superuser": False,
    },
    {
        "id": 4,
        "email": "admin@admin.com",
        "first_name": "Dmitry",
        "last_name": "Yankovskiy",
        "is_superuser": True,
        "is_active": True
    },
]
class BaseUserSchema(BaseModel):
    email: str
    first_name: str
    last_name: str

class UpdateUserSchema(BaseModel):
    first_name: str
    last_name: str

class CreateUserSchema(BaseUserSchema):
    pass

class UserListSchema(BaseUserSchema):
    id: int
    is_superuser: bool | None = None
    is_active: bool | None = None

