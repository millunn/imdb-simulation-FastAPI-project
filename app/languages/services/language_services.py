""" Language Services module """

from app.db.database import SessionLocal
from app.languages.repository import LanguageRepository


class LanguageServices:
    """Language model services"""

    @staticmethod
    def create_language(name, abbreviation):
        """Create new language"""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.create_language(name, abbreviation)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_language_by_id(language_id: str):
        """Get language by id"""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_language_by_id(language_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_language_by_name(name: str):
        """Get language by category"""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_language_by_name(name)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_language_by_abbreviation(abbreviation: str):
        """Get language by abbreviation"""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_language_by_abbreviation(abbreviation)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_languages():
        """Get all languages"""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.get_all_languages()
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_language_by_id(language_id: str):
        """Delete language by id"""
        try:
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                return language_repository.delete_language_by_id(language_id)
        except Exception as e:
            raise e from e
