from datetime import time
from pydantic import UUID4, BaseModel


class MovieSchema(BaseModel):
    id: UUID4
    title: str
    plot: str
    duration: time
    release_year: str
    director: str
    writer: str
    producer: str
    synopsis: str
    language_name: str
    genre_category: str

    class Config:
        orm_mode = True


class MovieSchemaIn(BaseModel):
    title: str
    plot: str
    duration: str
    release_year: str
    director: str
    writer: str
    producer: str
    synopsis: str
    language_name: str
    genre_category: str

    class Config:
        orm_mode = True
