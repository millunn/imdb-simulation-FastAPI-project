from fastapi import HTTPException, Response

from app.languages.services import LanguageServices


class LanguageController:
    @staticmethod
    def create_language(name, abbreviation):
        try:
            language = LanguageServices.create_language(name, abbreviation)
            return language
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_language_by_id(language_id: str):
        language = LanguageServices.get_language_by_id(language_id)
        if language:
            return language
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Language with provided id {language_id} does not exist",
            )

    @staticmethod
    def get_language_by_name(name: str):
        language = LanguageServices.get_language_by_name(name)
        if language:
            return language
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Language with provided name {name} does not exist",
            )

    @staticmethod
    def get_language_by_abbreviation(abbreviation: str):
        language = LanguageServices.get_language_by_abbreviation(abbreviation)
        if language:
            return language
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Language with provided abbreviation {abbreviation} does not exist",
            )

    @staticmethod
    def get_all_languages():
        languages = LanguageServices.get_all_languages()
        return languages

    @staticmethod
    def delete_language_by_id(language_id: str):
        try:
            LanguageServices.delete_language_by_id(language_id)
            return Response(
                content=f"Language with provided id - {language_id} is deleted"
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
