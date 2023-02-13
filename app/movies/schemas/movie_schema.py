from datetime import date, time
from pydantic import UUID4, BaseModel


class MovieSchema(BaseModel):
    id: UUID4
    title: str
    plot: str
    duration: time
    release_year: date
    director: str
    writer: str
    producer: str
    synopsis: str

    class Config:
        orm_mode = True


class MovieSchemaSchemaIn(BaseModel):
    title: str
    plot: str
    duration: str
    release_year: str
    director: str
    writer: str
    producer: str
    synopsis: str

    class Config:
        orm_mode = True
