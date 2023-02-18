from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.actors_actresses.exceptions import ActorActressNotFoundException

from app.tv_shows_and_series.exceptions import TVShowNotFoundException
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
            raise e

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
        return tv_show_actor_actress