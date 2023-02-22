""" Actor/Actress-Award-Movie Schema module """

from pydantic import UUID4, BaseModel
from app.actors_actresses.schemas.actor_actress_schema import ActorActressSchema
from app.awards.schemas import AwardSchema
from app.movies.schemas import MovieSchema


class ActorActressAwardMovieSchema(BaseModel):
    """ActorActressAwardMovie Schema for output"""

    id: UUID4
    actor_actress_id: UUID4
    award_id: UUID4
    movie_id: UUID4

    class Config:
        orm_mode = True


class ActorActressAwardMovieSchemaIn(BaseModel):
    """ActorActressAwardMovie Schema for input"""

    actor_actress_id: str
    award_id: str
    movie_id: str

    class Config:
        orm_mode = True


class AwardByActorActressSchemaOut(BaseModel):
    """AwardByActorActress Schema for output"""

    award: AwardSchema
    movie: MovieSchema
    actor_actress_id: UUID4

    class Config:
        orm_mode = True


class AwardByMovieSchemaOut(BaseModel):
    """AwardByMovie Schema for output"""

    actor_actress: ActorActressSchema
    award: AwardSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByAwardSchemaOut(BaseModel):
    """ActorActressByAward Schema for output"""

    actor_actress: ActorActressSchema
    movie: MovieSchema
    award_id: UUID4

    class Config:
        orm_mode = True


class ActorActressByMovieSchemaOut(BaseModel):
    """ActorActressByMovie Schema for output"""

    award: AwardSchema
    actor_actress: ActorActressSchema
    movie_id: UUID4

    class Config:
        orm_mode = True


class MostAwardedMovieActorsActressesSchema(BaseModel):
    """MostAwardedMovieActorsActresses Schema for output"""

    actor_actress_id: str
    number_of_awards: int

    class Config:
        orm_mode = True
