from pydantic import UUID4, BaseModel, PositiveInt


class MovieSchema(BaseModel):
    id: UUID4
    title: str
    plot: str
    duration: int
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
    duration: PositiveInt
    release_year: str
    director: str
    writer: str
    producer: str
    synopsis: str
    language_name: str
    genre_category: str

    class Config:
        orm_mode = True


class MovieGenreStatisticsSchema(BaseModel):
    genre_category: str
    category_count: int

    class Config:
        orm_mode = True


class MovieLanguageStatisticsSchema(BaseModel):
    language_name: str
    language_count: int

    class Config:
        orm_mode = True


class MovieDurationPerYearsSchema(BaseModel):
    release_year: str
    average_duration: int

    class Config:
        orm_mode = True
