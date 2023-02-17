from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.awards.exceptions import AwardNotFoundException
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.services import TvShowAwardServices


class TvShowAwardController:
    @staticmethod
    def create_tv_show_award(tv_show_id, award_id):
        try:
            tv_show_award = TvShowAwardServices.create_tv_show_award(
                tv_show_id, award_id
            )
            return tv_show_award

        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )

        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_by_award_id(award_id: str):
        try:
            tv_show = TvShowAwardServices.get_tv_show_by_award_id(award_id)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_tv_show_id(tv_show_id: str):
        try:
            award = TvShowAwardServices.get_award_by_tv_show_id(tv_show_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tv_shows_with_all_awards():
        try:
            tv_show_award_repository = (
                TvShowAwardServices.get_all_tv_shows_with_all_awards()
            )
            return tv_show_award_repository
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
