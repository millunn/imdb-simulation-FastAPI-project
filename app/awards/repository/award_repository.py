""" Award Repository module """

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.awards.exceptions import AwardNotFoundException
from app.awards.models import Award


class AwardRepository:
    """Award model repository"""

    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_award(self, category, subcategory):
        """Create new award"""
        try:
            award = Award(category, subcategory)
            self.db.add(award)
            self.db.commit()
            self.db.refresh(award)
            return award
        except IntegrityError as e:
            raise e from e

    def get_award_by_id(self, award_id: str):
        """Get award by id"""
        award = self.db.query(Award).filter(Award.id == award_id).first()
        if award is None:
            raise AwardNotFoundException(
                message=f"Award with provided id: {award_id} not found.", code=400
            )
        return award

    def get_award_by_category(self, category: str):
        """Get award by category"""
        award = self.db.query(Award).filter(Award.category.ilike(f"%{category}%")).all()
        if (award is None) or (award == []):
            raise AwardNotFoundException(
                message=f"Award with provided category: {category} not found.", code=400
            )
        return award

    def get_award_by_subcategory(self, subcategory: str):
        """Get award by subcategory"""
        award = (
            self.db.query(Award)
            .filter(Award.subcategory.ilike(f"%{subcategory}%"))
            .all()
        )
        if (award is None) or (award == []):
            raise AwardNotFoundException(
                message=f"Award with provided subcategory: {subcategory} not found.",
                code=400,
            )
        return award

    def get_all_awards(self):
        """Get all awards"""
        awards = self.db.query(Award).all()
        if (awards is None) or (awards == []):
            raise AwardNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return awards

    ##superuser
    def delete_award_by_id(self, award_id: str):
        """Delete award by id"""
        try:
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if award is None:
                raise AwardNotFoundException(code=400, message="Award not found")
            self.db.delete(award)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e

    def order_awards_by_category_decs(self):
        """Order awards by category in decsending order"""
        order_by_category_desc = (
            self.db.query(Award).order_by(Award.category.desc()).all()
        )
        return order_by_category_desc

    def order_awards_by_category_asc(self):
        """Order awards by category in acsending order"""
        order_by_category_asc = (
            self.db.query(Award).order_by(Award.category.asc()).all()
        )
        return order_by_category_asc
