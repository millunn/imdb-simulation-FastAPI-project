from pydantic import UUID4, BaseModel
from app.awards.schemas import AwardSchema
from app.movies.schemas import MovieSchema


class MovieAwardSchema(BaseModel):
    movie_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class MovieAwardSchemaIn(BaseModel):
    movie_id: UUID4
    award_id: UUID4

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
