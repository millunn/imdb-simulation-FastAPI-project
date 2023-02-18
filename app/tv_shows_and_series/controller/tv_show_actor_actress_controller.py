from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.services import TVShowActorActressServices


class TVShowActorActressController:
    @staticmethod
    def create_tv_show_actor_actress(tv_show_id, actor_actress_id):
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
            )
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )

        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_by_actor_actress_id(actor_actress_id: str):
        try:
            tv_show = TVShowActorActressServices.get_tv_show_by_actor_actress_id(
                actor_actress_id
            )
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_actor_actress_by_tv_show_id(tv_show_id: str):
        try:
            actor_actress = TVShowActorActressServices.get_actor_actress_by_tv_show_id(
                tv_show_id
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
    def get_all_tv_shows_with_all_actors_actresses():
        try:
            tv_show_actor_actress_repository = (
                TVShowActorActressServices.get_all_tv_shows_with_all_actors_actresses()
            )
            return tv_show_actor_actress_repository
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
