from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.awards.exceptions import AwardNotFoundException
from app.tv_shows_and_series.exceptions import (
    TVShowNotFoundException,
    TVShowAwardNotFoundException,
)
from app.tv_shows_and_series.services import TVShowAwardServices


class TVShowAwardController:
    @staticmethod
    def create_tv_show_award(tv_show_id, award_id):
        try:
            tv_show_award = TVShowAwardServices.create_tv_show_award(
                tv_show_id, award_id
            )
            return tv_show_award

        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_by_award_id(award_id: str):
        try:
            tv_show = TVShowAwardServices.get_tv_show_by_award_id(award_id)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_tv_show_id(tv_show_id: str):
        try:
            award = TVShowAwardServices.get_award_by_tv_show_id(tv_show_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_tv_shows_with_all_awards():
        try:
            tv_show_award_repository = (
                TVShowAwardServices.get_all_tv_shows_with_all_awards()
            )
            return tv_show_award_repository
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_top_five_most_awarded_tv_shows():
        try:
            tv_shows = TVShowAwardServices.get_top_five_most_awarded_tv_shows()
            return tv_shows
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_tv_show_award_by_id(tv_show_award_id: str):
        try:
            TVShowAwardServices.delete_tv_show_award_by_id(tv_show_award_id)
            return Response(
                content=f"Pair with provided id - {tv_show_award_id} is deleted"
            )
        except TVShowAwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
