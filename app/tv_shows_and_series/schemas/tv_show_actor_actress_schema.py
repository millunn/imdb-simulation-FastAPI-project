""" TVShowActorActress Schema module """

from pydantic import UUID4, BaseModel

from app.actors_actresses.schemas.actor_actress_schema import ActorActressSchema
from app.tv_shows_and_series.schemas.tv_show_schema import TVShowSchema


class TVShowActorActressSchema(BaseModel):
    """TVShowActorActress Schema for output"""

    id: UUID4
    tv_show_id: UUID4
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class TVShowActorActressSchemaIn(BaseModel):
    """TVShowActorActress Schema for input"""

    tv_show_id: str
    actor_actress_id: str

    class Config:
        orm_mode = True


class ActorActressByTVShowSchemaOut(BaseModel):
    """ActorActress by TVShow Schema for output"""

    actor_actress: ActorActressSchema
    tv_show_id: UUID4

    class Config:
        orm_mode = True


class TVShowByActorActressSchemaOut(BaseModel):
    """TVShow by ActorActress Schema for output"""

    tv_show: TVShowSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True
