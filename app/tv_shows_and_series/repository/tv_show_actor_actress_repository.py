from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.models.actor_actress import ActorActress
from app.tv_shows_and_series.exceptions import (
    TVShowNotFoundException,
    TVShowActorActressNotFoundException,
)
from app.tv_shows_and_series.models import TVShowActorActress


class TVShowActorActressRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_tv_show_actor_actress(self, tv_show_id, actor_actress_id):
        try:
            tv_show_actor_actress = TVShowActorActress(tv_show_id, actor_actress_id)
            self.db.add(tv_show_actor_actress)
            self.db.commit()
            self.db.refresh(tv_show_actor_actress)
            return tv_show_actor_actress
        except IntegrityError as e:
            raise e from e

    def get_tv_show_by_actor_actress_id(self, actor_actress_id: str):
        tv_show_by_actor_actress_id = (
            self.db.query(TVShowActorActress)
            .filter(TVShowActorActress.actor_actress_id == actor_actress_id)
            .all()
        )
        if (tv_show_by_actor_actress_id is None) or (tv_show_by_actor_actress_id == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided actor/actress id: {actor_actress_id} not found",
                code=400,
            )
        return tv_show_by_actor_actress_id

    def get_actor_actress_by_tv_show_id(self, tv_show_id: str):
        actor_actress_by_tv_show_id = (
            self.db.query(TVShowActorActress)
            .filter(TVShowActorActress.tv_show_id == tv_show_id)
            .all()
        )
        if (actor_actress_by_tv_show_id is None) or (actor_actress_by_tv_show_id == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided tv show id: {tv_show_id} not found",
                code=400,
            )
        return actor_actress_by_tv_show_id

    def get_all_tv_shows_with_all_actors_actresses(self):
        tv_show_actor_actress = self.db.query(TVShowActorActress).all()
        if (tv_show_actor_actress is None) or (tv_show_actor_actress == []):
            raise ActorActressNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return tv_show_actor_actress

    def get_actors_by_tv_show_id(self, tv_show_id: str):
        actors_by_tv_show_id = (
            self.db.query(ActorActress)
            .join(
                TVShowActorActress,
                ActorActress.id == TVShowActorActress.actor_actress_id,
            )
            .filter(
                ActorActress.gender == "m", TVShowActorActress.tv_show_id == tv_show_id
            )
            .all()
        )
        if (actors_by_tv_show_id is None) or (actors_by_tv_show_id == []):
            raise ActorActressNotFoundException(
                message=f"Actors with provided tv_show id: {tv_show_id} not found",
                code=400,
            )
        return actors_by_tv_show_id

    def get_actresses_by_tv_show_id(self, tv_show_id: str):
        actresses_by_tv_show_id = (
            self.db.query(ActorActress)
            .join(
                TVShowActorActress,
                ActorActress.id == TVShowActorActress.actor_actress_id,
            )
            .filter(
                ActorActress.gender == "f", TVShowActorActress.tv_show_id == tv_show_id
            )
            .all()
        )
        if (actresses_by_tv_show_id is None) or (actresses_by_tv_show_id == []):
            raise ActorActressNotFoundException(
                message=f"Actresses with provided tv_show id: {tv_show_id} not found",
                code=400,
            )
        return actresses_by_tv_show_id

    def delete_tv_show_actor_actress_by_id(self, tv_show_actor_actress_id: str):
        try:
            tv_show_actor_actress = (
                self.db.query(TVShowActorActress)
                .filter(TVShowActorActress.id == tv_show_actor_actress_id)
                .first()
            )
            if tv_show_actor_actress is None:
                raise TVShowActorActressNotFoundException(
                    code=400,
                    message=f"Pair with provided id: {tv_show_actor_actress_id} not found.",
                )
            self.db.delete(tv_show_actor_actress)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e
