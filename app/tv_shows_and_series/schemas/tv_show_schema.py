""" TVShow Schema module """

from pydantic import UUID4, BaseModel, PositiveInt


class TVShowSchema(BaseModel):
    """TVShow Schema for output"""

    id: UUID4
    title: str
    plot: str
    release_year: str
    creator: str
    seasons: int
    episodes: int
    episode_duration: int
    language_name: str
    genre_category: str

    class Config:
        orm_mode = True


class TVShowSchemaSchemaIn(BaseModel):
    """TVShow Schema for input"""

    title: str
    plot: str
    release_year: str
    creator: str
    seasons: PositiveInt
    episodes: PositiveInt
    episode_duration: PositiveInt
    language_name: str
    genre_category: str

    class Config:
        orm_mode = True


class TVShowGenreStatisticsSchema(BaseModel):
    """TVShow genre statistics Schema for output"""

    genre_category: str
    category_count: int

    class Config:
        orm_mode = True


class TVShowLanguageStatisticsSchema(BaseModel):
    """TVShow language statistics Schema for output"""

    language_name: str
    language_count: int

    class Config:
        orm_mode = True
