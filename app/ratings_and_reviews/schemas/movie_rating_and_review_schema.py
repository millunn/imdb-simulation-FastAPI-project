from pydantic import UUID4, BaseModel


class MovieRatingAndReviewSchema(BaseModel):
    id: UUID4
    grade: int
    comment: str
    movie_id: str
    user_id: str

    class Config:
        orm_mode = True


class MovieRatingAndReviewSchemaIn(BaseModel):
    grade: int
    comment: str
    movie_id: str
    user_id: str

    class Config:
        orm_mode = True


class MovieRatingAndReviewBySchemaOut(BaseModel):
    grade: int
    comment: str
    movie_id: str

    class Config:
        orm_mode = True


class MovieRatingAndReviewSchemaUpdateComment(BaseModel):
    comment: str

    class Config:
        orm_mode = True


class TopFiveMovieSchema(BaseModel):
    movie_id: str
    average_rating: float

    class Config:
        orm_mode = True


class MostRatedMoviesSchema(BaseModel):
    movie_id: str
    number_of_ratings: int

    class Config:
        orm_mode = True
