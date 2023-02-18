from pydantic import UUID4, BaseModel


class TVShowRatingAndReviewSchema(BaseModel):
    id: UUID4
    grade: int
    comment: str
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
    tv_show_id: str

    class Config:
        orm_mode = True


class TVShowRatingAndReviewSchemaUpdateComment(BaseModel):
    comment: str

    class Config:
        orm_mode = True
