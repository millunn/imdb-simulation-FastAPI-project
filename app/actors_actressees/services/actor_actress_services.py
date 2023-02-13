from app.actors_actressees.repository import ActorActressRepository
from app.db.database import SessionLocal


class ActorActressServices:
    @staticmethod
    def create_actor_actress(name, surname, gender, about):
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.create_actor_actress(
                    name, surname, gender, about
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_actor_actress_by_id(actor_actress_id: str):
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_actor_actress_by_name(name: str):
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_actor_actress_by_surname(surname: str):
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_surname(surname)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_actor_actresss():
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_all_actor_actresss()
        except Exception as e:
            raise e

    @staticmethod
    def delete_actor_actress_by_id(actor_actress_id: str):
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.delete_actor_actress_by_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e
