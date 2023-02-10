from app.db.database import SessionLocal
from app.languages.repository import LanguageRepository


class LanguageServices:
    @staticmethod
    def create_language(name, abbreviation):
        with SessionLocal() as db:
            try:
                language_repository = LanguageRepository(db)
                return language_repository.create_language(name, abbreviation)
            except Exception as e:
                raise e

    @staticmethod
    def get_language_by_id(language_id: str):
        with SessionLocal() as db:
            language_repository = LanguageRepository(db)
            return language_repository.get_language_by_id(language_id)

    @staticmethod
    def get_language_by_name(name: str):
        with SessionLocal() as db:
            language_repository = LanguageRepository(db)
            return language_repository.get_language_by_name(name)

    @staticmethod
    def get_language_by_abbreviation(abbreviation: str):
        with SessionLocal() as db:
            language_repository = LanguageRepository(db)
            return language_repository.get_language_by_abbreviation(abbreviation)

    @staticmethod
    def get_all_languages():
        with SessionLocal() as db:
            language_repository = LanguageRepository(db)
            return language_repository.get_all_languages()

    @staticmethod
    def delete_language_by_id(language_id: str):
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.delete_language_by_id(language_id)
        except Exception as e:
            raise e
