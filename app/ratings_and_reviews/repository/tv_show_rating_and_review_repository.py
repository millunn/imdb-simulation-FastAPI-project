from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.ratings_and_reviews.exceptions import TVShowRatingAndReviewNotFoundException
from app.ratings_and_reviews.models import TVShowRatingAndReview


class TVShowRatingAndReviewRepository:
    def __init__(self, db: Session):
        self.db = db

    # superuser
    def create_tv_show_rating_and_review(self, grade, comment, tv_show_id, user_id):
        try:
            tv_show_rating_and_review = TVShowRatingAndReview(
                grade, comment, tv_show_id, user_id
            )
            self.db.add(tv_show_rating_and_review)
            self.db.commit()
            self.db.refresh(tv_show_rating_and_review)
            return tv_show_rating_and_review
        except IntegrityError as e:
            raise e from e

    # superuser
    def get_tv_show_rating_and_review_by_id(self, tv_show_rating_and_review_id: str):
        tv_show_rating_and_review = (
            self.db.query(TVShowRatingAndReview)
            .filter(TVShowRatingAndReview.id == tv_show_rating_and_review_id)
            .first()
        )
        if tv_show_rating_and_review is None:
            raise TVShowRatingAndReviewNotFoundException(
                message=f"Tv show rating with provided id: {tv_show_rating_and_review_id} not found.",
                code=400,
            )
        return tv_show_rating_and_review

    def get_tv_show_rating_and_review_by_grade(self, grade: int):
        tv_show_rating_and_review = (
            self.db.query(TVShowRatingAndReview)
            .filter(TVShowRatingAndReview.grade == grade)
            .all()
        )
        if (tv_show_rating_and_review is None) or (tv_show_rating_and_review == []):
            raise TVShowRatingAndReviewNotFoundException(
                message=f"Tv show ratings with provided grade: {grade} not found.",
                code=400,
            )
        return tv_show_rating_and_review

    def get_tv_show_rating_and_review_by_tv_show_id(self, tv_show_id: str):
        tv_show_rating_and_review = (
            self.db.query(TVShowRatingAndReview)
            .filter(TVShowRatingAndReview.tv_show_id == tv_show_id)
            .all()
        )
        if (tv_show_rating_and_review is None) or (tv_show_rating_and_review == []):
            raise TVShowRatingAndReviewNotFoundException(
                message=f"Tv show ratings with provided tv_show id: {tv_show_id} not found.",
                code=400,
            )
        return tv_show_rating_and_review

    # superuser
    def get_tv_show_rating_and_review_by_user_id(self, user_id: str):
        tv_show_rating_and_review = (
            self.db.query(TVShowRatingAndReview)
            .filter(TVShowRatingAndReview.user_id == user_id)
            .all()
        )
        if (tv_show_rating_and_review is None) or (tv_show_rating_and_review == []):
            raise TVShowRatingAndReviewNotFoundException(
                message=f"Tv show ratings with provided user id: {user_id} not found.",
                code=400,
            )
        return tv_show_rating_and_review

    def get_all_tv_shows_ratings_and_reviews(self):
        tv_shows_ratings_and_reviews = self.db.query(TVShowRatingAndReview).all()
        if (tv_shows_ratings_and_reviews is None) or (
            tv_shows_ratings_and_reviews == []
        ):
            raise TVShowRatingAndReviewNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return tv_shows_ratings_and_reviews

    # superuser
    def delete_tv_show_rating_and_review_by_id(self, tv_show_rating_and_review_id: str):
        try:
            tv_show_rating_and_review = (
                self.db.query(TVShowRatingAndReview)
                .filter(TVShowRatingAndReview.id == tv_show_rating_and_review_id)
                .first()
            )
            if tv_show_rating_and_review is None:
                raise TVShowRatingAndReviewNotFoundException(
                    message=f"Tv show rating with provided id: {tv_show_rating_and_review_id} not found.",
                    code=400,
                )
            self.db.delete(tv_show_rating_and_review)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e

    def update_tv_show_rating_and_review_comment(
        self, tv_show_rating_and_review_id: str, comment: str
    ):
        try:
            tv_show_rating_and_review = (
                self.db.query(TVShowRatingAndReview)
                .filter(TVShowRatingAndReview.id == tv_show_rating_and_review_id)
                .first()
            )
            if tv_show_rating_and_review is None:
                raise TVShowRatingAndReviewNotFoundException(
                    f"TV show rating with provided id: {tv_show_rating_and_review_id} not found.",
                    400,
                )
            tv_show_rating_and_review.comment = comment
            tv_show_rating_and_review.comment_date = datetime.strftime(
                datetime.now(), "%Y-%m-%d, %H:%M:%S"
            )
            self.db.add(tv_show_rating_and_review)
            self.db.commit()
            self.db.refresh(tv_show_rating_and_review)
            return tv_show_rating_and_review
        except Exception as e:
            raise e from e
