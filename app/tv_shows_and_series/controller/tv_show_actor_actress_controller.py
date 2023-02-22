""" TvShow-ActorActress Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.tv_shows_and_series.exceptions import (
    TVShowNotFoundException,
    TVShowActorActressNotFoundException,
)
from app.tv_shows_and_series.services import TVShowActorActressServices


class TVShowActorActressController:
    """TvShow-ActorActress model controller"""

    @staticmethod
    def create_tv_show_actor_actress(tv_show_id, actor_actress_id):
        """Create new tv_show_actor_actress pair"""
        try:
            tv_show_actor_actress_award = (
                TVShowActorActressServices.create_tv_show_actor_actress(
                    tv_show_id, actor_actress_id
                )
            )
            return tv_show_actor_actress_award

        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e

        except IntegrityError as e:
            raise HTTPException(status_code=400, detail="Already in database") from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_by_actor_actress_id(actor_actress_id: str):
        """Get tv_show by actor_actress_id"""
        try:
            tv_show = TVShowActorActressServices.get_tv_show_by_actor_actress_id(
                actor_actress_id
            )
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_tv_show_id(tv_show_id: str):
        """Get actor_actress by tv_show_id"""
        try:
            actor_actress = TVShowActorActressServices.get_actor_actress_by_tv_show_id(
                tv_show_id
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
    def get_all_tv_shows_with_all_actors_actresses():
        """Get all tv_shows with all actors_actresses"""
        try:
            tv_show_actor_actress_repository = (
                TVShowActorActressServices.get_all_tv_shows_with_all_actors_actresses()
            )
            return tv_show_actor_actress_repository
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actors_by_tv_show_id(tv_show_id: str):
        """Get actors by tv_show_id"""
        try:
            actor_actress = TVShowActorActressServices.get_actors_by_tv_show_id(
                tv_show_id
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
    def get_actresses_by_tv_show_id(tv_show_id: str):
        """Get actresses by tv_show_id"""
        try:
            actresses_by_tv_show_id = (
                TVShowActorActressServices.get_actresses_by_tv_show_id(tv_show_id)
            )
            return actresses_by_tv_show_id
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_tv_show_actor_actress_by_id(tv_show_actor_actress_id: str):
        """Delete a pair actor_actress_tv_show by id"""
        try:
            TVShowActorActressServices.delete_tv_show_actor_actress_by_id(
                tv_show_actor_actress_id
            )
            return Response(
                content=f"Pair with provided id - {tv_show_actor_actress_id} is deleted"
            )
        except TVShowActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
