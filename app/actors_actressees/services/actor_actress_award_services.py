from sqlalchemy.exc import IntegrityError
from app.actors_actressees.repository import ActorActressAwardRepository
from app.actors_actressees.repository.actor_actress_repository import (
    ActorActressRepository,
)
from app.awards.repository.award_repository import AwardRepository
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
                award_repository = AwardRepository(db)
                award = award_repository.get_award_by_id(award_id)
                if actor_actress and award:
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
        with SessionLocal() as db:
            actor_actress_award_repository = ActorActressAwardRepository(db)
            return actor_actress_award_repository.get_award_by_actor_actress_id(
                actor_actress_id
            )

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        with SessionLocal() as db:
            actor_actress_award_repository = ActorActressAwardRepository(db)
            return actor_actress_award_repository.get_actor_actress_by_award_id(
                award_id
            )

    @staticmethod
    def get_all_actor_actresss_with_all_awards():
        with SessionLocal() as db:
            actor_actress_award_repository = ActorActressAwardRepository(db)
            return (
                actor_actress_award_repository.get_all_actor_actresss_with_all_awards()
            )
