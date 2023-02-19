from datetime import time
from pydantic import UUID4, BaseModel, PositiveInt


class TVShowSchema(BaseModel):
    id: UUID4
    title: str
    plot: str
    release_year: str
    creator: str
    seasons: int
    episodes: int
    episode_duration: time
    language_name: str
    genre_category: str

    class Config:
        orm_mode = True


class TVShowSchemaSchemaIn(BaseModel):
    title: str
    plot: str
    release_year: str
    creator: str
    seasons: PositiveInt
    episodes: PositiveInt
    episode_duration: str
    language_name: str
    genre_category: str

    class Config:
        orm_mode = True
