from pydantic import UUID4, BaseModel
from app.actors_actresses.schemas import ActorActressSchema
from app.tv_shows_and_series.schemas import TvShowSchema


class TvShowActorActressSchema(BaseModel):
    tv_show_id: UUID4
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class TvShowActorActressSchemaIn(BaseModel):
    tv_show_id: str
    actor_actress_id: str

    class Config:
        orm_mode = True


class ActorActressByTvShowSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class TvShowByActorActressSchemaOut(BaseModel):
    tv_show: TvShowSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True
