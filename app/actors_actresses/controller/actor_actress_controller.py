from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.actors_actresses.exceptions import (
    ActorActressNotFoundException,
)
from app.actors_actresses.services import ActorActressServices


class ActorActressController:
    @staticmethod
    def create_actor_actress(name, surname, gender, about):
        try:
            actor_actress = ActorActressServices.create_actor_actress(
                name, surname, gender, about
            )
            return actor_actress
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Actor/actress with provided data already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_actor_actress_by_id(actor_actress_id: str):
        try:
            actor_actress = ActorActressServices.get_actor_actress_by_id(
                actor_actress_id
            )
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_actor_actress_by_name(name: str):
        try:
            actor_actress = ActorActressServices.get_actor_actress_by_name(name)
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_actor_actress_by_surname(surname: str):
        try:
            actor_actress = ActorActressServices.get_actor_actress_by_surname(surname)
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_actor_actresss():
        try:
            actor_actresss = ActorActressServices.get_all_actor_actresss()
            return actor_actresss
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_actor_actress_by_id(actor_actress_id: str):
        try:
            ActorActressServices.delete_actor_actress_by_id(actor_actress_id)
            return Response(
                content=f"Actor/actress with provided id - {actor_actress_id} is deleted"
            )
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))