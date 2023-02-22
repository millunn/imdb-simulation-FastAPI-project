""" Actor/Actress Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import (
    ActorActressGenderException,
    ActorActressNotFoundException,
)
from app.actors_actresses.services import ActorActressServices


class ActorActressController:
    """Actor/Actress model controller"""

    @staticmethod
    def create_actor_actress(name, surname, gender, about):
        """Create new actor_actress"""
        try:
            actor_actress = ActorActressServices.create_actor_actress(
                name, surname, gender, about
            )
            return actor_actress
        except ActorActressGenderException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail="Actor/actress with provided data already exists.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_id(actor_actress_id: str):
        """Get actor_actress by id"""
        try:
            actor_actress = ActorActressServices.get_actor_actress_by_id(
                actor_actress_id
            )
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_name(name: str):
        """Get actor_actress by name"""
        try:
            actor_actress = ActorActressServices.get_actor_actress_by_name(name)
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_surname(surname: str):
        """Get actor_actress by surname"""
        try:
            actor_actress = ActorActressServices.get_actor_actress_by_surname(surname)
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_gender(gender: str):
        """Get actor_actress by gender"""
        try:
            actor_actress = ActorActressServices.get_actor_actress_by_gender(gender)
            return actor_actress
        except ActorActressGenderException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_actors_actresses():
        """Get all actors_actresses"""
        try:
            actor_actresss = ActorActressServices.get_all_actors_actresses()
            return actor_actresss
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_actor_actress_by_id(actor_actress_id: str):
        """Delete actor_actress by id"""
        try:
            ActorActressServices.delete_actor_actress_by_id(actor_actress_id)
            return Response(
                content=f"Actor/actress with provided id - {actor_actress_id} is deleted"
            )
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_actor_actress_by_name_decs():
        """Order actor_actress by name in decsending order"""
        try:
            order_by_name_desc = ActorActressServices.order_actor_actress_by_name_decs()
            return order_by_name_desc
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_actor_actress_by_name_asc():
        """Order actor_actress by name in acsending order"""
        try:
            order_by_title_asc = ActorActressServices.order_actor_actress_by_name_asc()
            return order_by_title_asc
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_gender_statistics():
        """Get gender statistics"""
        try:
            gender_statistics = ActorActressServices.get_gender_statistics()
            return gender_statistics
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_actor_actress_about_section(actor_actress_id: str, about: str):
        """Update actor_actress about section"""
        try:
            actor_actress = ActorActressServices.update_actor_actress_about_section(
                actor_actress_id, about
            )
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
