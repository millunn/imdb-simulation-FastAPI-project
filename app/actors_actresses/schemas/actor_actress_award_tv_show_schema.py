from pydantic import UUID4, BaseModel

from app.actors_actresses.schemas import ActorActressSchema
from app.awards.schemas import AwardSchema
from app.tv_shows_and_series.schemas import TVShowSchema


class ActorActressAwardTVShowSchema(BaseModel):
    actor_actress_id: UUID4
    award_id: UUID4
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class ActorActressAwardTVShowSchemaIn(BaseModel):
    actor_actress_id: str
    award_id: str
    tv_show_id: str

    class Config:
        orm_mode = True


class AwardByActorActressSchemaOut(BaseModel):
    award: AwardSchema
    tv_show: TVShowSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class AwardByTVShowSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    award: AwardSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByAwardSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    tv_show: TVShowSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByTVShowSchemaOut(BaseModel):
    award: AwardSchema
    actor_actress: ActorActressSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class MostAwardedTVShowActorsActressesSchema(BaseModel):
    actor_actress_id: str
    number_of_awards: int

    class Config:
        orm_mode = True
