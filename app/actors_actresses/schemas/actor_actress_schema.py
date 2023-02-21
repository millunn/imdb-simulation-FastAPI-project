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


class ActorActressGenderStatisticsSchema(BaseModel):
    gender: str
    gender_count: int

    class Config:
        orm_mode = True


class ActorActressSchemaUpdateAboutSection(BaseModel):
    about: str

    class Config:
        orm_mode = True
