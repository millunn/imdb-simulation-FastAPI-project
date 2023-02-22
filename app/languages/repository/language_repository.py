""" Language Repository module """

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.languages.exceptions import LanguageNotFoundException
from app.languages.models import Language


class LanguageRepository:
    """Language model repository"""

    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_language(self, name, abbreviation):
        """Create new language"""
        try:
            language = Language(name, abbreviation)
            self.db.add(language)
            self.db.commit()
            self.db.refresh(language)
            return language
        except IntegrityError as e:
            raise e from e

    def get_language_by_id(self, language_id: str):
        """Get language by id"""
        language = self.db.query(Language).filter(Language.id == language_id).first()
        if language is None:
            raise LanguageNotFoundException(
                f"Language with provided id: {language_id} not found.", 400
            )
        return language

    def get_language_by_name(self, name: str):
        """Get language by category"""
        language = (
            self.db.query(Language).filter(Language.name.ilike(f"%{name}%")).all()
        )
        if (language is None) or (language == []):
            raise LanguageNotFoundException(
                f"Language with provided category: {name} not found.", 400
            )
        return language

    def get_language_by_abbreviation(self, abbreviation: str):
        """Get language by abbreviation"""
        language = (
            self.db.query(Language)
            .filter(Language.abbreviation.ilike(f"%{abbreviation}%"))
            .all()
        )
        if (language is None) or (language == []):
            raise LanguageNotFoundException(
                f"Language with provided abbreviation: {abbreviation} not found.", 400
            )
        return language

    def get_all_languages(self):
        """Get all languages"""
        languages = self.db.query(Language).all()
        if (languages is None) or (languages == []):
            raise LanguageNotFoundException(f"The list is empty!", 400)
        return languages

    ##superuser
    def delete_language_by_id(self, language_id: str):
        """Delete language by id"""
        try:
            language = (
                self.db.query(Language).filter(Language.id == language_id).first()
            )
            if language is None:
                raise LanguageNotFoundException(
                    f"Language with provided id: {language_id} not found.", 400
                )
            self.db.delete(language)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e
