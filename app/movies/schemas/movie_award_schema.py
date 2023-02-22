""" MovieAward Schema module """

from pydantic import UUID4, BaseModel

from app.awards.schemas.award_schema import AwardSchema
from app.movies.schemas.movie_schema import MovieSchema


class MovieAwardSchema(BaseModel):
    """MovieAward Schema for output"""

    id: UUID4
    movie_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class MovieAwardSchemaIn(BaseModel):
    """MovieAward Schema for input"""

    movie_id: str
    award_id: str

    class Config:
        orm_mode = True


class AwardByMovieSchemaOut(BaseModel):
    """Award by Movie Schema for output"""

    award: AwardSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class MovieByAwardSchemaOut(BaseModel):
    """Movie by Award Schema for output"""

    movie: MovieSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class MostAwardedMoviesSchema(BaseModel):
    """Most awarded Movies Schema for output"""

    movie_id: str
    number_of_awards: int

    class Config:
        orm_mode = True
