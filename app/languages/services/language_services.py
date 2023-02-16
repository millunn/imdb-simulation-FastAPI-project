import uuid
from app.db.database import SessionLocal
from app.languages.repository import LanguageRepository


class LanguageServices:
    @staticmethod
    def create_language(name, abbreviation):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.create_language(name, abbreviation)
        except Exception as e:
            raise e

    @staticmethod
    def get_language_by_id(language_id: str):
        try:
            uuid.UUID(str(language_id))
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_language_by_id(language_id)
        except ValueError:
            raise Exception(f"Provided id: {language_id} not uuid")
        except Exception as e:
            raise e

    @staticmethod
    def get_language_by_name(name: str):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_language_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_language_by_abbreviation(abbreviation: str):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_language_by_abbreviation(abbreviation)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_languages():
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_all_languages()
        except Exception as e:
            raise e

    @staticmethod
    def delete_language_by_id(language_id: str):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.delete_language_by_id(language_id)
        except Exception as e:
            raise e
