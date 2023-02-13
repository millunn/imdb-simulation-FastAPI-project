from pydantic import UUID4, BaseModel
from app.awards.schemas import AwardSchema
from app.actors_actressees.schemas import ActorActressSchema


class ActorActressAwardSchema(BaseModel):
    actor_actress_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class ActorActressAwardSchemaIn(BaseModel):
    actor_actress_id: UUID4
    award_id: UUID4

    class Config:
        orm_mode = True


class AwardByActorActressSchemaOut(BaseModel):
    actor_actress_id: UUID4
    award: AwardSchema

    class Config:
        orm_mode = True


class ActorActressByAwardSchemaOut(BaseModel):
    award_id: UUID4
    actor_actress: ActorActressSchema

    class Config:
        orm_mode = True
