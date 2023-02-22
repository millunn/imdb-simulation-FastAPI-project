""" Actor/Actress Schema module """

from pydantic import UUID4, BaseModel


class ActorActressSchema(BaseModel):
    """ActorActress Schema for output"""

    id: UUID4
    name: str
    surname: str
    gender: str
    about: str

    class Config:
        orm_mode = True


class ActorActressSchemaIn(BaseModel):
    """ActorActress Schema for input"""

    name: str
    surname: str
    gender: str
    about: str

    class Config:
        orm_mode = True


class ActorActressGenderStatisticsSchema(BaseModel):
    """ActorActressGenderStatistics Schema for output"""

    gender: str
    gender_count: int

    class Config:
        orm_mode = True


class ActorActressSchemaUpdateAboutSection(BaseModel):
    """ActorActressAboutSection Schema for update"""

    about: str

    class Config:
        orm_mode = True
