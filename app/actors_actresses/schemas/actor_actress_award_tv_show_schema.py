from pydantic import UUID4, BaseModel
from app.awards.schemas import AwardSchema
from app.actors_actresses.schemas import ActorActressSchema
from app.tv_shows_and_series.schemas import TvShowSchema


class ActorActressAwardTvShowSchema(BaseModel):
    actor_actress_id: UUID4
    award_id: UUID4
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class ActorActressAwardTvShowSchemaIn(BaseModel):
    actor_actress_id: str
    award_id: str
    tv_show_id: str

    class Config:
        orm_mode = True


class AwardByActorActressSchemaOut(BaseModel):
    award: AwardSchema
    tv_show: TvShowSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class AwardByTvShowSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    award: AwardSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByAwardSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    tv_show: TvShowSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByTvShowSchemaOut(BaseModel):
    award: AwardSchema
    actor_actress: ActorActressSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True
