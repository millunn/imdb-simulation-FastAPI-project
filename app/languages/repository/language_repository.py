from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.languages.models import Language


class LanguageRepository:
    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_language(self, name, abbreviation):
        try:
            language = Language(name, abbreviation)
            self.db.add(language)
            self.db.commit()
            self.db.refresh(language)
            return language
        except IntegrityError as e:
            raise e

    def get_language_by_id(self, language_id: str):
        language = self.db.query(Language).filter(Language.id == language_id).first()
        return language

    def get_language_by_name(self, name: str):
        language = self.db.query(Language).filter(Language.name == name).first()
        return language

    def get_language_by_abbreviation(self, abbreviation: str):
        language = (
            self.db.query(Language)
            .filter(Language.abbreviation == abbreviation)
            .first()
        )
        return language

    def get_all_languages(self):
        languages = self.db.query(Language).all()
        return languages

    ##superuser
    def delete_language_by_id(self, language_id: str):
        try:
            language = (
                self.db.query(Language).filter(Language.id == language_id).first()
            )
            self.db.delete(language)
            self.db.commit()
            return True
        except Exception as e:
            raise e
