from uuid import UUID

from fastapi_users import schemas
from pydantic import BaseModel


class UserBase(schemas.BaseUser[int]):
    username: str
    first_name: str
    last_name: str
    role_id: int = 1
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    token: UUID

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class UserRead(schemas.BaseUser[int]):
    id: int
    token: UUID

    class Config:
        from_attributes = True


class UserTokenSchema(BaseModel):
    token: str
