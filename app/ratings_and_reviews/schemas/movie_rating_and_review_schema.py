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