from fastapi import HTTPException, Response

from app.actors_actressees.services import ActorActressServices


class ActorActressController:
    @staticmethod
    def create_actor_actress(name, surname, gender, about):
        try:
            actor_actress = ActorActressServices.create_actor_actress(
                name, surname, gender, about
            )
            return actor_actress
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_actor_actress_by_id(actor_actress_id: str):
        actor_actress = ActorActressServices.get_actor_actress_by_id(actor_actress_id)
        if actor_actress:
            return actor_actress
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Actor/actress with provided id {actor_actress_id} does not exist",
            )

    @staticmethod
    def get_actor_actress_by_name(name: str):
        actor_actress = ActorActressServices.get_actor_actress_by_name(name)
        if actor_actress:
            return actor_actress
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Actor/actress with provided name {name} does not exist",
            )

    @staticmethod
    def get_actor_actress_by_surname(surname: str):
        actor_actress = ActorActressServices.get_actor_actress_by_surname(surname)
        if actor_actress:
            return actor_actress
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Actor/actress with provided surname {surname} does not exist",
            )

    @staticmethod
    def get_all_actor_actresss():
        actor_actresss = ActorActressServices.get_all_actor_actresss()
        return actor_actresss

    @staticmethod
    def delete_actor_actress_by_id(actor_actress_id: str):
        try:
            ActorActressServices.delete_actor_actress_by_id(actor_actress_id)
            return Response(
                content=f"actor_actress with provided id - {actor_actress_id} is deleted"
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
