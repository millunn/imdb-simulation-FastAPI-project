from pydantic import UUID4, BaseModel
from app.awards.schemas import AwardSchema
from app.tv_shows_and_series.schemas import TVShowSchema


class TVShowAwardSchema(BaseModel):
    tv_show_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class TVShowAwardSchemaIn(BaseModel):
    tv_show_id: str
    award_id: str

    class Config:
        orm_mode = True


class AwardByTVShowSchemaOut(BaseModel):
    award: AwardSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class TVShowByAwardSchemaOut(BaseModel):
    tv_show: TVShowSchema
    award_id: UUID4

    class Config:
        orm_mode = True
