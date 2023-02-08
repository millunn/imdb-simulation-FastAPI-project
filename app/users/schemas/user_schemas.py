from pydantic import UUID4, BaseModel, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    id: UUID4
    name: Optional[str]
    surname: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaLogIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
