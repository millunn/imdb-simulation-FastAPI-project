from pydantic import UUID4, BaseModel
from app.actors_actresses.schemas import ActorActressSchema
from app.tv_shows_and_series.schemas import TVShowSchema


class TVShowActorActressSchema(BaseModel):
    tv_show_id: UUID4
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class TVShowActorActressSchemaIn(BaseModel):
    tv_show_id: str
    actor_actress_id: str

    class Config:
        orm_mode = True


class ActorActressByTVShowSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class TVShowByActorActressSchemaOut(BaseModel):
    tv_show: TVShowSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True