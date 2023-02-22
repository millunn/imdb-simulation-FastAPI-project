""" TVShowAward Schema module """

from pydantic import UUID4, BaseModel

from app.awards.schemas.award_schema import AwardSchema
from app.tv_shows_and_series.schemas.tv_show_schema import TVShowSchema


class TVShowAwardSchema(BaseModel):
    """TVShowAward Schema for output"""

    id: UUID4
    tv_show_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class TVShowAwardSchemaIn(BaseModel):
    """TVShowAward Schema for input"""

    tv_show_id: str
    award_id: str

    class Config:
        orm_mode = True


class AwardByTVShowSchemaOut(BaseModel):
    """Award by TVShow Schema for output"""

    award: AwardSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class TVShowByAwardSchemaOut(BaseModel):
    """TVShow by Award Schema for output"""

    tv_show: TVShowSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class MostAwardedTVShowsSchema(BaseModel):
    """Most awarded TVShows Schema for output"""

    tv_show_id: str
    number_of_awards: int

    class Config:
        orm_mode = True
