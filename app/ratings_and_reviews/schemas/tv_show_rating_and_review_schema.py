from pydantic import UUID4, BaseModel


class TVShowRatingAndReviewSchema(BaseModel):
    id: UUID4
    grade: int
    comment: str
    comment_date: str
    tv_show_id: str
    user_id: str

    class Config:
        orm_mode = True


class TVShowRatingAndReviewSchemaIn(BaseModel):
    grade: int
    comment: str
    tv_show_id: str
    user_id: str

    class Config:
        orm_mode = True


class TVShowRatingAndReviewBySchemaOut(BaseModel):
    grade: int
    comment: str
    comment_date: str
    tv_show_id: str

    class Config:
        orm_mode = True


class TVShowRatingAndReviewSchemaUpdateComment(BaseModel):
    comment: str

    class Config:
        orm_mode = True


class TopFiveTVShowSchema(BaseModel):
    tv_show_id: str
    average_rating: float

    class Config:
        orm_mode = True


class MostRatedTVShowSchema(BaseModel):
    tv_show_id: str
    number_of_ratings: int

    class Config:
        orm_mode = True
