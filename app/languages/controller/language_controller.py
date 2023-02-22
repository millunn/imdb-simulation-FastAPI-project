""" Language Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.languages.exceptions import LanguageNotFoundException
from app.languages.services import LanguageServices


class LanguageController:
    """Language model controller"""

    @staticmethod
    def create_language(name, abbreviation):
        """Create new language"""
        try:
            language = LanguageServices.create_language(name, abbreviation)
            return language
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Language with provided name - {name} already exists.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_language_by_id(language_id: str):
        """Get language by id"""
        try:
            language = LanguageServices.get_language_by_id(language_id)
            return language
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_language_by_name(name: str):
        """Get language by category"""
        try:
            language = LanguageServices.get_language_by_name(name)
            return language
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_language_by_abbreviation(abbreviation: str):
        """Get language by abbreviation"""
        try:
            language = LanguageServices.get_language_by_abbreviation(abbreviation)
            return language
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_languages():
        """Get all languages"""
        try:
            languages = LanguageServices.get_all_languages()
            return languages
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_language_by_id(language_id: str):
        """Delete language by id"""
        try:
            LanguageServices.delete_language_by_id(language_id)
            return Response(
                content=f"Language with provided id - {language_id} is deleted"
            )
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
