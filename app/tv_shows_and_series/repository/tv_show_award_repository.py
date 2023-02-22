from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.awards.exceptions import AwardNotFoundException
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.models import TVShowAward


class TVShowAwardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_tv_show_award(self, tv_show_id, award_id):
        try:
            tv_show_award = TVShowAward(tv_show_id, award_id)
            self.db.add(tv_show_award)
            self.db.commit()
            self.db.refresh(tv_show_award)
            return tv_show_award
        except IntegrityError as e:
            raise e

    def get_tv_show_by_award_id(self, award_id: str):
        tv_show_by_award_id = (
            self.db.query(TVShowAward).filter(TVShowAward.award_id == award_id).all()
        )
        if (tv_show_by_award_id is None) or (tv_show_by_award_id == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided award id: {award_id} not found",
                code=400,
            )
        return tv_show_by_award_id

    def get_award_by_tv_show_id(self, tv_show_id: str):
        award_by_tv_show_id = (
            self.db.query(TVShowAward)
            .filter(TVShowAward.tv_show_id == tv_show_id)
            .all()
        )
        if (award_by_tv_show_id is None) or (award_by_tv_show_id == []):
            raise AwardNotFoundException(
                message=f"Award with provided tv show id: {tv_show_id} not found",
                code=400,
            )
        return award_by_tv_show_id

    def get_all_tv_shows_with_all_awards(self):
        tv_show_award = self.db.query(TVShowAward).all()
        if (tv_show_award is None) or (tv_show_award == []):
            raise AwardNotFoundException(
                message=f"The list is empty!",
                code=400,
            )
        return tv_show_award

    def get_top_five_most_awarded_tv_shows(self):
        tv_show_rating_and_review = (
            self.db.query(TVShowAward)
            .group_by(TVShowAward.tv_show_id)
            .order_by(desc("number_of_awards"))
            .limit(5)
            .values(
                TVShowAward.tv_show_id.label("tv_show_id"),
                func.count(TVShowAward.award_id).label("number_of_awards"),
            )
        )
        return tv_show_rating_and_review
