from pydantic import UUID4, BaseModel

from app.awards.schemas.award_schema import AwardSchema
from app.tv_shows_and_series.schemas.tv_show_schema import TVShowSchema


class TVShowAwardSchema(BaseModel):
    id: UUID4
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


class MostAwardedTVShowsSchema(BaseModel):
    tv_show_id: str
    number_of_awards: int

    class Config:
        orm_mode = True
