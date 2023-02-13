from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.actors_actressees.exceptions import ActorActressNotFoundException
from app.actors_actressees.repository import ActorActressAwardRepository
from app.actors_actressees.repository import (
    ActorActressRepository,
)
from app.awards.exceptions.award_exceptions import AwardNotFoundException
from app.awards.repository import AwardRepository
from app.db.database import SessionLocal


class ActorActressAwardServices:
    @staticmethod
    def create_actor_actress_award(actor_actress_id, award_id):
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
                actor_actress_award_repository = ActorActressAwardRepository(db)
                return actor_actress_award_repository.create_actor_actress_award(
                    actor_actress_id, award_id
                )
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        try:
            with SessionLocal() as db:
                award_actor_actress_repository = ActorActressAwardRepository(db)
                return award_actor_actress_repository.get_award_by_actor_actress_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        try:
            with SessionLocal() as db:
                actor_actress_award_repository = ActorActressAwardRepository(db)
                return actor_actress_award_repository.get_actor_actress_by_award_id(
                    award_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_all_actor_actresss_with_all_awards():
        try:
            with SessionLocal() as db:
                actor_actress_award_repository = ActorActressAwardRepository(db)
                return (
                    actor_actress_award_repository.get_all_actor_actresss_with_all_awards()
                )
        except Exception as e:
            raise e
