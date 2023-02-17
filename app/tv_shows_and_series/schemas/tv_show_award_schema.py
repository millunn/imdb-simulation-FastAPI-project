from pydantic import UUID4, BaseModel
from app.awards.schemas import AwardSchema
from app.tv_shows_and_series.schemas import TvShowSchema


class TvShowAwardSchema(BaseModel):
    tv_show_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class TvShowAwardSchemaIn(BaseModel):
    tv_show_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class AwardByTvShowSchemaOut(BaseModel):
    award: AwardSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class TvShowByAwardSchemaOut(BaseModel):
    tv_show: TvShowSchema
    award_id: UUID4

    class Config:
        orm_mode = True
