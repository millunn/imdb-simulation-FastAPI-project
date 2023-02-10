from pydantic import UUID4, BaseModel


class ActorActressSchema(BaseModel):
    id: UUID4
    name: str
    surname: str
    gender: str
    about: str

    class Config:
        orm_mode = True


class ActorActressSchemaIn(BaseModel):
    name: str
    surname: str
    gender: str
    about: str

    class Config:
        orm_mode = True
