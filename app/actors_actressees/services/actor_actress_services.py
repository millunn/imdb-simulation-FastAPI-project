from app.actors_actressees.repository import ActorActressRepository
from app.db.database import SessionLocal


class ActorActressServices:
    @staticmethod
    def create_actor_actress(name, surname, gender, about):
        with SessionLocal() as db:
            try:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.create_actor_actress(
                    name, surname, gender, about
                )
            except Exception as e:
                raise e

    @staticmethod
    def get_actor_actress_by_id(actor_actress_id: str):
        with SessionLocal() as db:
            actor_actress_repository = ActorActressRepository(db)
            return actor_actress_repository.get_actor_actress_by_id(actor_actress_id)

    @staticmethod
    def get_actor_actress_by_name(name: str):
        with SessionLocal() as db:
            actor_actress_repository = ActorActressRepository(db)
            return actor_actress_repository.get_actor_actress_by_name(name)

    @staticmethod
    def get_actor_actress_by_surname(surname: str):
        with SessionLocal() as db:
            actor_actress_repository = ActorActressRepository(db)
            return actor_actress_repository.get_actor_actress_by_surname(surname)

    @staticmethod
    def get_all_actor_actresss():
        with SessionLocal() as db:
            actor_actress_repository = ActorActressRepository(db)
            return actor_actress_repository.get_all_actor_actresss()

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
