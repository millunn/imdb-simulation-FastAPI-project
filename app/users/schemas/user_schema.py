from pydantic import UUID4, BaseModel, EmailStr


class UserSchema(BaseModel):
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


class UserSchemaUpdateName(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserSchemaUpdateSurname(BaseModel):
    surname: str

    class Config:
        orm_mode = True


class UserSchemaUpdateActivity(BaseModel):
    is_active: bool

    class Config:
        orm_mode = True