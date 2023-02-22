""" Actor/Actress-Award-TvShow Schema module """

from pydantic import UUID4, BaseModel

from app.actors_actresses.schemas.actor_actress_schema import ActorActressSchema
from app.awards.schemas.award_schema import AwardSchema
from app.tv_shows_and_series.schemas.tv_show_schema import TVShowSchema


class ActorActressAwardTVShowSchema(BaseModel):
    """ActorActressAwardTVShow Schema for input"""

    id: UUID4
    actor_actress_id: UUID4
    award_id: UUID4
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class ActorActressAwardTVShowSchemaIn(BaseModel):
    """AwardByActorActress Schema for output"""

    actor_actress_id: str
    award_id: str
    tv_show_id: str

    class Config:
        orm_mode = True


class AwardByActorActressSchemaOut(BaseModel):
    """AwardByTVShow Schema for output"""

    award: AwardSchema
    tv_show: TVShowSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class AwardByTVShowSchemaOut(BaseModel):
    """ActorActressByAward Schema for output"""

    actor_actress: ActorActressSchema
    award: AwardSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByAwardSchemaOut(BaseModel):
    """ActorActressByTVShow Schema for output"""

    actor_actress: ActorActressSchema
    tv_show: TVShowSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByTVShowSchemaOut(BaseModel):
    """ActorActressByTVShow Schema for output"""

    award: AwardSchema
    actor_actress: ActorActressSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class MostAwardedTVShowActorsActressesSchema(BaseModel):
    """MostAwardedTVShowActorsActresses Schema for output"""

    actor_actress_id: str
    number_of_awards: int

    class Config:
        orm_mode = True
