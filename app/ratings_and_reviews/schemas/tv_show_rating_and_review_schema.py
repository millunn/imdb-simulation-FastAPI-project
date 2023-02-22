""" TVShowRatingAndReview Schema module """

from pydantic import UUID4, BaseModel


class TVShowRatingAndReviewSchema(BaseModel):
    """TVShowRatingAndReview Schema for output"""

    id: UUID4
    grade: int
    comment: str
    comment_date: str
    tv_show_id: str
    user_id: str

    class Config:
        orm_mode = True


class TVShowRatingAndReviewSchemaIn(BaseModel):
    """TVShowRatingAndReview Schema for input"""

    grade: int
    comment: str
    tv_show_id: str
    user_id: str

    class Config:
        orm_mode = True


class TVShowRatingAndReviewBySchemaOut(BaseModel):
    """TVShowRatingAndReview by attribute Schema for output"""

    grade: int
    comment: str
    comment_date: str
    tv_show_id: str

    class Config:
        orm_mode = True


class TVShowRatingAndReviewSchemaUpdateComment(BaseModel):
    """TVShowRatingAndReview Schema for update"""

    comment: str

    class Config:
        orm_mode = True


class TopFiveTVShowSchema(BaseModel):
    """Top five tv shows Schema for output"""

    tv_show_id: str
    average_rating: float

    class Config:
        orm_mode = True


class MostRatedTVShowSchema(BaseModel):
    """Most rated tv shows Schema for output"""

    tv_show_id: str
    number_of_ratings: int

    class Config:
        orm_mode = True
