""" MovieRatingAndReview Schema module """

from pydantic import UUID4, BaseModel


class MovieRatingAndReviewSchema(BaseModel):
    """MovieRatingAndReview Schema for output"""

    id: UUID4
    grade: int
    comment: str
    comment_date: str
    movie_id: str
    user_id: str

    class Config:
        orm_mode = True


class MovieRatingAndReviewSchemaIn(BaseModel):
    """MovieRatingAndReview Schema for input"""

    grade: int
    comment: str
    movie_id: str
    user_id: str

    class Config:
        orm_mode = True


class MovieRatingAndReviewBySchemaOut(BaseModel):
    """MovieRatingAndReview by attribute Schema for output"""

    grade: int
    comment: str
    comment_date: str
    movie_id: str

    class Config:
        orm_mode = True


class MovieRatingAndReviewSchemaUpdateComment(BaseModel):
    """MovieRatingAndReview Schema for update"""

    comment: str

    class Config:
        orm_mode = True


class TopFiveMovieSchema(BaseModel):
    """Top five movies Schema for output"""

    movie_id: str
    average_rating: float

    class Config:
        orm_mode = True


class MostRatedMoviesSchema(BaseModel):
    """Most rated movies Schema for output"""

    movie_id: str
    number_of_ratings: int

    class Config:
        orm_mode = True
