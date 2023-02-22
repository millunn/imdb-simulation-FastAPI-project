""" MovieActorActress Schema module """

from pydantic import UUID4, BaseModel

from app.actors_actresses.schemas.actor_actress_schema import ActorActressSchema
from app.movies.schemas.movie_schema import MovieSchema


class MovieActorActressSchema(BaseModel):
    """MovieActorActress Schema for output"""

    id: UUID4
    movie_id: UUID4
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class MovieActorActressSchemaIn(BaseModel):
    """MovieActorActress Schema for input"""

    movie_id: str
    actor_actress_id: str

    class Config:
        orm_mode = True


class ActorActressByMovieSchemaOut(BaseModel):
    """ActorActress by Movie Schema for output"""

    actor_actress: ActorActressSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class MovieByActorActressSchemaOut(BaseModel):
    """Movie by ActorActress Schema for output"""

    movie: MovieSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True
