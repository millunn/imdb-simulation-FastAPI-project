from app.actors_actresses.exceptions import ActorActressGenderException
from app.actors_actresses.repository import ActorActressRepository
from app.db.database import SessionLocal


class ActorActressServices:
    @staticmethod
    def create_actor_actress(name, surname, gender, about):
        try:
            if (gender.lower() != "m") and (gender.lower() != "f"):
                raise ActorActressGenderException(
                    message=f"Gender must be M for male or F for female!",
                    code=400,
                )
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
    def get_actor_actress_by_gender(gender: str):
        try:
            if (gender.lower() != "m") and (gender.lower() != "f"):
                raise ActorActressGenderException(
                    message=f"Gender must be M for male or F for female!",
                    code=400,
                )
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_gender(gender)
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
    def get_all_actors_actresses():
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_all_actors_actresses()
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

    @staticmethod
    def order_actor_actress_by_name_decs():
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.order_actor_actress_by_name_decs()
        except Exception as e:
            raise e

    @staticmethod
    def order_actor_actress_by_name_asc():
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.order_actor_actress_by_name_asc()
        except Exception as e:
            raise e

    @staticmethod
    def get_gender_statistics():
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_gender_statistics()
        except Exception as e:
            raise e

    @staticmethod
    def update_actor_actress_about_section(actor_actress_id: str, about: str):
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.update_actor_actress_about_section(
                    actor_actress_id, about
                )
        except Exception as e:
            raise e
