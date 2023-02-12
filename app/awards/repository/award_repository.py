from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.awards.exceptions import AwardNotFoundException
from app.awards.models import Award


class AwardRepository:
    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_award(self, category, subcategory):
        try:
            award = Award(category, subcategory)
            self.db.add(award)
            self.db.commit()
            self.db.refresh(award)
            return award
        except IntegrityError as e:
            raise e

    def get_award_by_id(self, award_id: str):
        award = self.db.query(Award).filter(Award.id == award_id).first()
        return award

    def get_award_by_category(self, category: str):
        award = self.db.query(Award).filter(Award.category == category).first()
        return award

    def get_award_by_subcategory(self, subcategory: str):
        award = self.db.query(Award).filter(Award.subcategory == subcategory).first()
        return award

    def get_all_awards(self):
        awards = self.db.query(Award).all()
        return awards

    ##superuser
    def delete_award_by_id(self, award_id: str):
        try:
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if award is None:
                raise AwardNotFoundException(code=400, message="Award not found")
            self.db.delete(award)
            self.db.commit()
            return True
        except Exception as e:
            raise e
