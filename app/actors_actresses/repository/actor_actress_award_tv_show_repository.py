""" Actor/Actress-Award-TvShow Repository module """

from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.exceptions.actor_actress_award_tv_show_exceptions import (
    ActorActressAwardTVShowNotFoundException,
)
from app.actors_actresses.models import ActorActressAwardTvShow
from app.awards.exceptions import AwardNotFoundException


class ActorActressAwardTvShowRepository:
    """Actor/Actress-Award-TvShow model repository"""

    def __init__(self, db: Session):
        self.db = db

    def create_actor_actress_award_tv_show(
        self, actor_actress_id, award_id, tv_show_id
    ):
        """Create new actor_actress_award_tv_show"""
        try:
            actor_actress_award_tv_show = ActorActressAwardTvShow(
                actor_actress_id, award_id, tv_show_id
            )
            self.db.add(actor_actress_award_tv_show)
            self.db.commit()
            self.db.refresh(actor_actress_award_tv_show)
            return actor_actress_award_tv_show
        except IntegrityError as e:
            raise e from e

    def get_award_by_actor_actress_id(self, actor_actress_id: str):
        """Get award by actor_actress_id"""
        award_by_actor_actress_id = (
            self.db.query(ActorActressAwardTvShow)
            .filter(ActorActressAwardTvShow.actor_actress_id == actor_actress_id)
            .all()
        )
        if (award_by_actor_actress_id is None) or (award_by_actor_actress_id == []):
            raise AwardNotFoundException(
                message=f"Award with provided actor/actress id: {actor_actress_id} not found",
                code=400,
            )
        return award_by_actor_actress_id

    def get_award_by_tv_show_id(self, tv_show_id: str):
        """Get award by tv_show_id"""
        award_by_tv_show_id = (
            self.db.query(ActorActressAwardTvShow)
            .filter(ActorActressAwardTvShow.tv_show_id == tv_show_id)
            .all()
        )
        if (award_by_tv_show_id is None) or (award_by_tv_show_id == []):
            raise AwardNotFoundException(
                message=f"Award with provided tv show id: {tv_show_id} not found",
                code=400,
            )
        return award_by_tv_show_id

    def get_actor_actress_by_award_id(self, award_id: str):
        """Get actor_actress by award_id"""
        actor_actress_by_award_id = (
            self.db.query(ActorActressAwardTvShow)
            .filter(ActorActressAwardTvShow.award_id == award_id)
            .all()
        )
        if (actor_actress_by_award_id is None) or (actor_actress_by_award_id == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided award id: {award_id} not found",
                code=400,
            )
        return actor_actress_by_award_id

    def get_actor_actress_by_tv_show_id(self, tv_show_id: str):
        """Get actor_actress by tv_show_id"""
        actor_actress_by_tv_show_id = (
            self.db.query(ActorActressAwardTvShow)
            .filter(ActorActressAwardTvShow.tv_show_id == tv_show_id)
            .all()
        )
        if (actor_actress_by_tv_show_id is None) or (actor_actress_by_tv_show_id == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided tv show id: {tv_show_id} not found",
                code=400,
            )
        return actor_actress_by_tv_show_id

    def get_all_actors_actresses_with_all_awards_all_tv_shows(self):
        """Get all actors_actresses with all awards and all tv_shows"""
        actor_actress_award_tv_show = self.db.query(ActorActressAwardTvShow).all()
        if (actor_actress_award_tv_show is None) or (actor_actress_award_tv_show == []):
            raise ActorActressNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return actor_actress_award_tv_show

    def get_top_five_most_awarded_tv_show_actors_actresses(self):
        """Get top five most awarded tv_show actors actresses"""
        actor_actress_award_tv_show = (
            self.db.query(ActorActressAwardTvShow)
            .group_by(ActorActressAwardTvShow.actor_actress_id)
            .order_by(desc("number_of_awards"))
            .limit(5)
            .values(
                ActorActressAwardTvShow.actor_actress_id.label("actor_actress_id"),
                func.count(ActorActressAwardTvShow.award_id).label("number_of_awards"),
            )
        )
        return actor_actress_award_tv_show

    def delete_actor_actress_award_tv_show_by_id(
        self, actor_actress_award_tv_show_id: str
    ):
        """Delete a pair actor_actress_award_tv_show by id"""
        try:
            actor_actress_award_tv_show = (
                self.db.query(ActorActressAwardTvShow)
                .filter(ActorActressAwardTvShow.id == actor_actress_award_tv_show_id)
                .first()
            )
            if actor_actress_award_tv_show is None:
                raise ActorActressAwardTVShowNotFoundException(
                    message=f"Pair with provided id: {actor_actress_award_tv_show_id} not found.",
                    code=400,
                )
            self.db.delete(actor_actress_award_tv_show)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e
