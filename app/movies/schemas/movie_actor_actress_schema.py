from pydantic import UUID4, BaseModel
from app.actors_actressees.schemas import ActorActressSchema
from app.movies.schemas import MovieSchema


class MovieActorActressSchema(BaseModel):
    movie_id: UUID4
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class MovieActorActressSchemaIn(BaseModel):
    movie_id: UUID4
    actor_actress_id: UUID4

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
