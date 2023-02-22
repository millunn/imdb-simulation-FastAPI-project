from pydantic import UUID4, BaseModel

from app.awards.schemas.award_schema import AwardSchema
from app.movies.schemas.movie_schema import MovieSchema


class MovieAwardSchema(BaseModel):
    movie_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class MovieAwardSchemaIn(BaseModel):
    movie_id: str
    award_id: str

    class Config:
        orm_mode = True


class AwardByMovieSchemaOut(BaseModel):
    award: AwardSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class MovieByAwardSchemaOut(BaseModel):
    movie: MovieSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class MostAwardedMoviesSchema(BaseModel):
    movie_id: str
    number_of_awards: int

    class Config:
        orm_mode = True
