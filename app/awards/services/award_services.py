""" Award Services module """

from app.awards.exceptions import AwardNotFoundException
from app.awards.repository import AwardRepository
from app.db.database import SessionLocal


class AwardServices:
    """Award model services"""

    @staticmethod
    def create_award(category, subcategory):
        """Create new award"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.create_award(category, subcategory)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_id(award_id: str):
        """Get award by id"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_award_by_id(award_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_category(category: str):
        """Get award by category"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_award_by_category(category)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_subcategory(subcategory: str):
        """Get award by subcategory"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_award_by_subcategory(subcategory)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_awards():
        """Get all awards"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_all_awards()
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_award_by_id(award_id: str):
        """Delete award by id"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                if award_repository.delete_award_by_id(award_id):
                    return True
                raise AwardNotFoundException(code=400, message="Award doesn't exist.")
        except Exception as e:
            raise e from e

    @staticmethod
    def order_awards_by_category_decs():
        """Order awards by category in decsending order"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.order_awards_by_category_decs()
        except Exception as e:
            raise e from e

    @staticmethod
    def order_awards_by_category_asc():
        """Order awards by category in acsending order"""
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.order_awards_by_category_asc()
        except Exception as e:
            raise e from e
