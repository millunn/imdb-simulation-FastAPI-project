""" Actor/Actress-Award-TvShow Services module """

from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.repository import (
    ActorActressAwardTvShowRepository,
    ActorActressRepository,
)
from app.awards.exceptions.award_exceptions import AwardNotFoundException
from app.awards.repository import AwardRepository
from app.db.database import SessionLocal
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.repository import TVShowRepository


class ActorActressAwardTvShowServices:
    """Actor/Actress-Award-TvShow model services"""

    @staticmethod
    def create_actor_actress_award_tv_show(actor_actress_id, award_id, tv_show_id):
        """Create new actor_actress_award_tv_show"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                actor_actress = actor_actress_repository.get_actor_actress_by_id(
                    actor_actress_id
                )
                if actor_actress is None:
                    raise ActorActressNotFoundException(
                        message=f"Actor/actress with provided id: {actor_actress_id} not found.",
                        code=400,
                    )
                award_repository = AwardRepository(db)
                award = award_repository.get_award_by_id(award_id)
                if award is None:
                    raise AwardNotFoundException(
                        message=f"Award with provided id: {award_id} not found.",
                        code=400,
                    )
                actor_actress_award_tv_show_repository = (
                    ActorActressAwardTvShowRepository(db)
                )
                tv_show_repository = TVShowRepository(db)
                tv_show = tv_show_repository.get_tv_show_by_id(tv_show_id)
                if tv_show is None:
                    raise TVShowNotFoundException(
                        message=f"Tv show with provided id: {tv_show_id} not found.",
                        code=400,
                    )
                return actor_actress_award_tv_show_repository.create_actor_actress_award_tv_show(
                    actor_actress_id,
                    award_id,
                    tv_show_id,
                )
        except IntegrityError as e:
            raise e from e
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        """Get award by actor_actress_id"""
        try:
            with SessionLocal() as db:
                award_actor_actress_repository = ActorActressAwardTvShowRepository(db)
                return award_actor_actress_repository.get_award_by_actor_actress_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_tv_show_id(tv_show_id: str):
        """Get award by tv_show_id"""
        try:
            with SessionLocal() as db:
                award_tv_show_repository = ActorActressAwardTvShowRepository(db)
                return award_tv_show_repository.get_award_by_tv_show_id(tv_show_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        """Get actor_actress by award_id"""
        try:
            with SessionLocal() as db:
                actor_actress_award_tv_show_repository = (
                    ActorActressAwardTvShowRepository(db)
                )
                return actor_actress_award_tv_show_repository.get_actor_actress_by_award_id(
                    award_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_tv_show_id(tv_show_id: str):
        """Get actor_actress by tv_show_id"""
        try:
            with SessionLocal() as db:
                actor_actress_tv_show_repository = ActorActressAwardTvShowRepository(db)
                return actor_actress_tv_show_repository.get_actor_actress_by_tv_show_id(
                    tv_show_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_actors_actresses_with_all_awards_all_tv_shows():
        """Get all actors_actresses with all awards and all tv_shows"""
        try:
            with SessionLocal() as db:
                actor_actress_award_tv_show_repository = (
                    ActorActressAwardTvShowRepository(db)
                )
                return (
                    actor_actress_award_tv_show_repository.get_all_actors_actresses_with_all_awards_all_tv_shows()
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_top_five_most_awarded_tv_show_actors_actresses():
        """Get top five most awarded tv_show actors actresses"""
        try:
            with SessionLocal() as db:
                actor_actress_award_tv_show_repository = (
                    ActorActressAwardTvShowRepository(db)
                )
                return (
                    actor_actress_award_tv_show_repository.get_top_five_most_awarded_tv_show_actors_actresses()
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_actor_actress_award_tv_show_by_id(actor_actress_award_tv_show_id: str):
        """Delete a pair actor_actress_award_tv_show by id"""
        try:
            with SessionLocal() as db:
                actor_actress_award_tv_show_repository = (
                    ActorActressAwardTvShowRepository(db)
                )
                return actor_actress_award_tv_show_repository.delete_actor_actress_award_tv_show_by_id(
                    actor_actress_award_tv_show_id
                )
        except Exception as e:
            raise e from e
