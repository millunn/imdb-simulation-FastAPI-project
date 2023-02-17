import uuid
from sqlalchemy.exc import IntegrityError
from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.repository import (
    ActorActressRepository,
)
from app.db.database import SessionLocal
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.repository import (
    TVShowRepository,
    TvShowActorActressRepository,
)


class TvShowActorActressServices:
    @staticmethod
    def create_tv_show_actor_actress(tv_show_id, actor_actress_id):
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                tv_show = tv_show_repository.get_tv_show_by_id(tv_show_id)
                if tv_show is None:
                    raise TVShowNotFoundException(
                        message=f"Tv show with provided id: {tv_show_id} not found.",
                        code=400,
                    )
                actor_actress_repository = ActorActressRepository(db)
                actor_actress = actor_actress_repository.get_actor_actress_by_id(
                    actor_actress_id
                )
                if actor_actress is None:
                    raise ActorActressNotFoundException(
                        message=f"Actor/actress with provided id: {actor_actress_id} not found.",
                        code=400,
                    )
                tv_show_actor_actress_repository = TvShowActorActressRepository(db)
                return tv_show_actor_actress_repository.create_tv_show_actor_actress(
                    tv_show_id, actor_actress_id
                )
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def get_tv_show_by_actor_actress_id(actor_actress_id: str):
        try:
            uuid.UUID(str(actor_actress_id))
            with SessionLocal() as db:
                award_actor_actress_repository = TvShowActorActressRepository(db)
                return award_actor_actress_repository.get_tv_show_by_actor_actress_id(
                    actor_actress_id
                )
        except ValueError:
            raise Exception(f"Provided id: {actor_actress_id} not uuid")
        except Exception as e:
            raise e

    @staticmethod
    def get_actor_actress_by_tv_show_id(tv_show_id: str):
        try:
            uuid.UUID(str(tv_show_id))
            with SessionLocal() as db:
                actor_actress_tv_show_repository = TvShowActorActressRepository(db)
                return actor_actress_tv_show_repository.get_actor_actress_by_tv_show_id(
                    tv_show_id
                )
        except ValueError:
            raise Exception(f"Provided id: {tv_show_id} not uuid")
        except Exception as e:
            raise e

    @staticmethod
    def get_all_tv_shows_with_all_actors_actresses():
        try:
            with SessionLocal() as db:
                tv_show_actor_actress_repository = TvShowActorActressRepository(db)
                return (
                    tv_show_actor_actress_repository.get_all_tv_shows_with_all_actors_actresses()
                )
        except Exception as e:
            raise e
