from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.models import ActorActressAwardTvShow
from app.awards.exceptions import AwardNotFoundException


class ActorActressAwardTvShowRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_actor_actress_award_tv_show(
        self, actor_actress_id, award_id, tv_show_id
    ):
        try:
            actor_actress_award_tv_show = ActorActressAwardTvShow(
                actor_actress_id, award_id, tv_show_id
            )
            self.db.add(actor_actress_award_tv_show)
            self.db.commit()
            self.db.refresh(actor_actress_award_tv_show)
            return actor_actress_award_tv_show
        except IntegrityError as e:
            raise e

    def get_award_by_actor_actress_id(self, actor_actress_id: str):
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

    def get_all_actor_actress_with_all_awards_all_tv_shows(self):
        actor_actress_award_tv_show = self.db.query(ActorActressAwardTvShow).all()
        return actor_actress_award_tv_show

    def get_top_five_most_awarded_tv_show_actors_actresses(self):
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
