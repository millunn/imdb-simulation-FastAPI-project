""" TVShowAward Services module """
from sqlalchemy.exc import IntegrityError

from app.awards.exceptions import AwardNotFoundException
from app.awards.repository.award_repository import AwardRepository
from app.db.database import SessionLocal
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.repository import TVShowAwardRepository, TVShowRepository


class TVShowAwardServices:
    """TVShowAward model services"""

    @staticmethod
    def create_tv_show_award(tv_show_id, award_id):
        """Create new tv_show_award"""
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                tv_show = tv_show_repository.get_tv_show_by_id(tv_show_id)
                if tv_show is None:
                    raise TVShowNotFoundException(
                        message=f"Tv show with provided id: {tv_show_id} not found.",
                        code=400,
                    )
                award_repository = AwardRepository(db)
                award = award_repository.get_award_by_id(award_id)
                if award is None:
                    raise AwardNotFoundException(
                        message=f"Award with provided id: {award_id} not found.",
                        code=400,
                    )
                tv_show_award_repository = TVShowAwardRepository(db)
                return tv_show_award_repository.create_tv_show_award(
                    tv_show_id, award_id
                )
        except IntegrityError as e:
            raise e from e
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_by_award_id(award_id: str):
        """Get tv_show by award_id"""
        try:
            with SessionLocal() as db:
                tv_show_award_repository = TVShowAwardRepository(db)
                return tv_show_award_repository.get_tv_show_by_award_id(award_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_tv_show_id(tv_show_id: str):
        """Get award by tv_show_id"""
        try:
            with SessionLocal() as db:
                award_tv_show_repository = TVShowAwardRepository(db)
                return award_tv_show_repository.get_award_by_tv_show_id(tv_show_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_tv_shows_with_all_awards():
        """Get all tv_shows with all awards"""
        try:
            with SessionLocal() as db:
                tv_show_award_repository = TVShowAwardRepository(db)
                return tv_show_award_repository.get_all_tv_shows_with_all_awards()
        except Exception as e:
            raise e from e

    @staticmethod
    def get_top_five_most_awarded_tv_shows():
        """Get top five most awarded tv_shows"""
        try:
            with SessionLocal() as db:
                tv_show_award_repository = TVShowAwardRepository(db)
                return tv_show_award_repository.get_top_five_most_awarded_tv_shows()
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_tv_show_award_by_id(tv_show_award_id: str):
        """Delete a pair tv_show_award by id"""
        try:
            with SessionLocal() as db:
                tv_show_award_repository = TVShowAwardRepository(db)
                return tv_show_award_repository.delete_tv_show_award_by_id(
                    tv_show_award_id
                )
        except Exception as e:
            raise e from e
