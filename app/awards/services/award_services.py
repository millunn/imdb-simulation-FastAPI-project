from app.awards.exceptions import AwardNotFoundException
from app.awards.repository import AwardRepository
from app.db.database import SessionLocal


class AwardServices:
    @staticmethod
    def create_award(category, subcategory):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.create_award(category, subcategory)
        except Exception as e:
            raise e

    @staticmethod
    def get_award_by_id(award_id: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_award_by_id(award_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_award_by_category(category: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_award_by_category(category)
        except Exception as e:
            raise e

    @staticmethod
    def get_award_by_subcategory(subcategory: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_award_by_subcategory(subcategory)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_awards():
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_all_awards()
        except Exception as e:
            raise e

    @staticmethod
    def delete_award_by_id(award_id: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                if award_repository.delete_study_programme_by_id(award_id):
                    return True
                raise AwardNotFoundException(code=400, message="Award doesn't exist.")
        except Exception as e:
            raise e
