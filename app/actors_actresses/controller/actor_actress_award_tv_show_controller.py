from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.services import ActorActressAwardTvShowServices
from app.awards.exceptions import AwardNotFoundException
from app.tv_shows_and_series.exceptions import TVShowNotFoundException


class ActorActressAwardTvShowController:
    @staticmethod
    def create_actor_actress_award_tv_show(actor_actress_id, award_id, tv_show_id):
        try:
            actor_actress_award_tv_show = (
                ActorActressAwardTvShowServices.create_actor_actress_award_tv_show(
                    actor_actress_id,
                    award_id,
                    tv_show_id,
                )
            )
            return actor_actress_award_tv_show
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail="Already in database") from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        try:
            award = ActorActressAwardTvShowServices.get_award_by_actor_actress_id(
                actor_actress_id
            )
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_tv_show_id(tv_show_id: str):
        try:
            award = ActorActressAwardTvShowServices.get_award_by_tv_show_id(tv_show_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        try:
            actor_actress = (
                ActorActressAwardTvShowServices.get_actor_actress_by_award_id(award_id)
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
    def get_actor_actress_by_tv_show_id(tv_show_id: str):
        try:
            actor_actress = (
                ActorActressAwardTvShowServices.get_actor_actress_by_tv_show_id(
                    tv_show_id
                )
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
    def get_all_actors_actresses_with_all_awards_all_tv_shows():
        try:
            actor_actress_award_tv_show = (
                ActorActressAwardTvShowServices.get_all_actors_actresses_with_all_awards_all_tv_shows()
            )
            return actor_actress_award_tv_show
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_top_five_most_awarded_tv_show_actors_actresses():
        try:
            actor_actress_award_tv_show = (
                ActorActressAwardTvShowServices.get_top_five_most_awarded_tv_show_actors_actresses()
            )
            return actor_actress_award_tv_show
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
