from app.awards.repository import AwardRepository
from app.db.database import SessionLocal


class AwardServices:
    @staticmethod
    def create_award(category, subcategory):
        with SessionLocal() as db:
            try:
                award_repository = AwardRepository(db)
                return award_repository.create_award(category, subcategory)
            except Exception as e:
                raise e

    @staticmethod
    def get_award_by_id(award_id: str):
        with SessionLocal() as db:
            award_repository = AwardRepository(db)
            return award_repository.get_award_by_id(award_id)

    @staticmethod
    def get_award_by_category(category: str):
        with SessionLocal() as db:
            award_repository = AwardRepository(db)
            return award_repository.get_award_by_category(category)

    @staticmethod
    def get_award_by_subcategory(subcategory: str):
        with SessionLocal() as db:
            award_repository = AwardRepository(db)
            return award_repository.get_award_by_subcategory(subcategory)

    @staticmethod
    def get_all_awards():
        with SessionLocal() as db:
            award_repository = AwardRepository(db)
            return award_repository.get_all_awards()

    @staticmethod
    def delete_award_by_id(award_id: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.delete_award_by_id(award_id)
        except Exception as e:
            raise e
