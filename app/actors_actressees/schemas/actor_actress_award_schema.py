from pydantic import UUID4, BaseModel
from app.awards.schemas import AwardSchema
from app.actors_actressees.schemas import ActorActressSchema
from app.movies.schemas import MovieSchema


class ActorActressAwardMovieSchema(BaseModel):
    actor_actress_id: UUID4
    award_id: UUID4
    movie_id: UUID4

    class Config:
        orm_mode = True


class ActorActressAwardMovieSchemaIn(BaseModel):
    actor_actress_id: UUID4
    award_id: UUID4
    movie_id: UUID4

    class Config:
        orm_mode = True


class AwardByActorActressSchemaOut(BaseModel):
    award: AwardSchema
    movie: MovieSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class AwardByMovieSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    award: AwardSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByAwardSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    movie: MovieSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByMovieSchemaOut(BaseModel):
    award: AwardSchema
    actor_actress: ActorActressSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class MovieByActorActressSchemaOut(BaseModel):
    award: AwardSchema
    movie: MovieSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class MovieByAwardSchemaOut(BaseModel):
    actor_actress: ActorActressSchema
    movie: MovieSchema
    award_id: UUID4

    class Config:
        orm_mode = True