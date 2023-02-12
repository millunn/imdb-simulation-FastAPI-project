from pydantic import UUID4, BaseModel


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
