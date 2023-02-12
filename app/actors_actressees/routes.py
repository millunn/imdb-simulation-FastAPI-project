from fastapi import APIRouter, Depends
from app.actors_actressees.controller import (
    ActorActressController,
    ActorActressAwardController,
)
from app.actors_actressees.schemas import (
    ActorActressSchema,
    ActorActressSchemaIn,
    ActorActressAwardSchema,
    ActorActressAwardSchemaIn,
)


from app.users.controller.user_auth_controller import JWTBearer

actor_actress_router = APIRouter(tags=["actor_actress"], prefix="/api/actor_actresss")
actor_actress_award_router = APIRouter(
    tags=["actor_actress_award"], prefix="/api/actor_actress_award"
)


@actor_actress_router.post("/add-new-actor-actress", response_model=ActorActressSchema)
def create_actor_actress(actor_actress: ActorActressSchemaIn):
    return ActorActressController.create_actor_actress(
        actor_actress.name,
        actor_actress.surname,
        actor_actress.gender,
        actor_actress.about,
    )


@actor_actress_router.get("/id", response_model=ActorActressSchema)
def get_actor_actress_by_id(actor_actress_id: str):
    return ActorActressController.get_actor_actress_by_id(actor_actress_id)


@actor_actress_router.get("/name", response_model=list[ActorActressSchema])
def get_actor_actress_by_name(name: str):
    return ActorActressController.get_actor_actress_by_name(name)


@actor_actress_router.get("/surname", response_model=ActorActressSchema)
def get_actor_actress_by_surname(surname: str):
    return ActorActressController.get_actor_actress_by_surname(surname)


@actor_actress_router.get(
    "/get-all-actor-actresses", response_model=list[ActorActressSchema]
)
def get_all_actor_actresss():
    return ActorActressController.get_all_actor_actresss()


@actor_actress_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_actor_actress_by_id(actor_actress_id: str):
    return ActorActressController.delete_actor_actress_by_id(actor_actress_id)


@actor_actress_award_router.post(
    "/add-new-actor-actress-award", response_model=ActorActressAwardSchema
)
def create_actor_actress_award(actor_actress_award: ActorActressAwardSchemaIn):
    return ActorActressAwardController.create_actor_actress_award(
        actor_actress_award.actor_actress_id,
        actor_actress_award.award_id,
    )


@actor_actress_award_router.get(
    "/actor-actress-id", response_model=list[ActorActressAwardSchema]
)
def get_award_by_actor_actress_id(actor_actress_id: str):
    return ActorActressAwardController.get_award_by_actor_actress_id(actor_actress_id)


@actor_actress_award_router.get(
    "/award-id", response_model=list[ActorActressAwardSchema]
)
def get_actor_actress_by_award_id(award_id: str):
    return ActorActressAwardController.get_actor_actress_by_award_id(award_id)


@actor_actress_award_router.get(
    "/get-all-actor_actresses-with-all-awards",
    response_model=list[ActorActressAwardSchema],
)
def get_all_actor_actresss_with_all_awards():
    return ActorActressAwardController.get_all_actor_actresss_with_all_awards()
