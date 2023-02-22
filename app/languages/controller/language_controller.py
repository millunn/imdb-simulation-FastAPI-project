from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.languages.exceptions import LanguageNotFoundException
from app.languages.services import LanguageServices


class LanguageController:
    @staticmethod
    def create_language(name, abbreviation):
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
