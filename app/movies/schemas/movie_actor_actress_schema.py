from pydantic import UUID4, BaseModel

from app.actors_actresses.schemas.actor_actress_schema import ActorActressSchema
from app.movies.schemas.movie_schema import MovieSchema


class MovieActorActressSchema(BaseModel):
    id: UUID4
    movie_id: UUID4
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class MovieActorActressSchemaIn(BaseModel):
    movie_id: str
    actor_actress_id: str

    class Config:
        orm_mode = True


class ActorActressByMovieSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class MovieByActorActressSchemaOut(BaseModel):
    movie: MovieSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True
