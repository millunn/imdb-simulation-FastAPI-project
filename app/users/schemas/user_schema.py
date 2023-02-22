""" Award Schema module """

from pydantic import UUID4, BaseModel, EmailStr


class UserSchema(BaseModel):
    """User Schema for output"""

    id: UUID4
    name: str
    surname: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    """User Schema for input"""

    name: str
    surname: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaLogIn(BaseModel):
    """User Schema for Log In"""

    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaUpdateName(BaseModel):
    """User update Schema for Name"""

    name: str

    class Config:
        orm_mode = True


class UserSchemaUpdateSurname(BaseModel):
    """User update Schema for Surname"""

    surname: str

    class Config:
        orm_mode = True


class UserSchemaUpdateActivity(BaseModel):
    """User update Schema for Activity"""

    is_active: bool

    class Config:
        orm_mode = True
