""" Actor/Actress Services module """

from app.actors_actresses.exceptions import ActorActressGenderException
from app.actors_actresses.repository import ActorActressRepository
from app.db.database import SessionLocal


class ActorActressServices:
    """Actor/Actress model services"""

    @staticmethod
    def create_actor_actress(name, surname, gender, about):
        """Create new actor_actress"""
        try:
            if (gender.lower() != "m") and (gender.lower() != "f"):
                raise ActorActressGenderException(
                    message="Gender must be M for male or F for female!",
                    code=400,
                )
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.create_actor_actress(
                    name, surname, gender, about
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_id(actor_actress_id: str):
        """Get actor_actress by id"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_name(name: str):
        """Get actor_actress by name"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_name(name)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_gender(gender: str):
        """Get actor_actress by surname"""
        try:
            if (gender.lower() != "m") and (gender.lower() != "f"):
                raise ActorActressGenderException(
                    message="Gender must be M for male or F for female!",
                    code=400,
                )
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_gender(gender)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_surname(surname: str):
        """Get actor_actress by gender"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_actor_actress_by_surname(surname)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_actors_actresses():
        """Get all actors_actresses"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_all_actors_actresses()
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_actor_actress_by_id(actor_actress_id: str):
        """Delete actor_actress by id"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.delete_actor_actress_by_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def order_actor_actress_by_name_decs():
        """Order actor_actress by name in decsending order"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.order_actor_actress_by_name_decs()
        except Exception as e:
            raise e from e

    @staticmethod
    def order_actor_actress_by_name_asc():
        """Order actor_actress by name in acsending order"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.order_actor_actress_by_name_asc()
        except Exception as e:
            raise e from e

    @staticmethod
    def get_gender_statistics():
        """Get gender statistics"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.get_gender_statistics()
        except Exception as e:
            raise e from e

    @staticmethod
    def update_actor_actress_about_section(actor_actress_id: str, about: str):
        """Update actor_actress about section"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                return actor_actress_repository.update_actor_actress_about_section(
                    actor_actress_id, about
                )
        except Exception as e:
            raise e from e
