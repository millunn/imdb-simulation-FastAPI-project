from fastapi import APIRouter, Depends
from app.actors_actressees.controller import ActorActressController
from app.actors_actressees.schemas import (
    ActorActressSchema,
    ActorActressSchemaIn,
)


from app.users.controller.user_auth_controller import JWTBearer

actor_actress_router = APIRouter(tags=["actor_actress"], prefix="/api/actor_actresss")


@actor_actress_router.post("/add-new-actor_actress", response_model=ActorActressSchema)
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
    "/get-all-actor_actresses", response_model=list[ActorActressSchema]
)
def get_all_actor_actresss():
    return ActorActressController.get_all_actor_actresss()


@actor_actress_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_actor_actress_by_id(actor_actress_id: str):
    return ActorActressController.delete_actor_actress_by_id(actor_actress_id)
