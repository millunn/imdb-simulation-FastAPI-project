""" TVShowRatingAndReview Services module """

from app.db.database import SessionLocal
from app.ratings_and_reviews.exceptions import TVShowRatingAndReviewGradeException
from app.ratings_and_reviews.repository import TVShowRatingAndReviewRepository
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.repository import TVShowRepository
from app.users.exceptions import UserNotFoundException
from app.users.repository import UserRepository


class TVShowRatingAndReviewServices:
    """TVShowRatingAndReview model services"""

    @staticmethod
    def create_tv_show_rating_and_review(grade, comment, tv_show_id, user_id):
        """Create new tv_show_rating_and_review pair"""
        try:
            if 1 > grade or grade > 5:
                raise TVShowRatingAndReviewGradeException(
                    message="Grade must be in range of 1 to 5.",
                    code=400,
                )
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                tv_show = tv_show_repository.get_tv_show_by_id(tv_show_id)
                if tv_show is None:
                    raise TVShowNotFoundException(
                        message=f"Tv show with provided tv show id: {tv_show_id} not found.",
                        code=400,
                    )
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_id(user_id)
                if user is None:
                    raise UserNotFoundException(
                        message=f"User with provided user id: {user_id} not found.",
                        code=400,
                    )
                tv_show_rating_and_review_repository = TVShowRatingAndReviewRepository(
                    db
                )
                return tv_show_rating_and_review_repository.create_tv_show_rating_and_review(
                    grade, comment, tv_show_id, user_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_rating_and_review_by_id(tv_show_rating_and_review_id: str):
        """Get tv_show_rating_and_review by id"""
        try:
            with SessionLocal() as db:
                tv_show_rating_and_review_repository = TVShowRatingAndReviewRepository(
                    db
                )
                return tv_show_rating_and_review_repository.get_tv_show_rating_and_review_by_id(
                    tv_show_rating_and_review_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_rating_and_review_by_grade(grade: int):
        """Get tv_show_rating_and_review by grade"""
        try:
            with SessionLocal() as db:
                tv_show_rating_and_review_repository = TVShowRatingAndReviewRepository(
                    db
                )
                return tv_show_rating_and_review_repository.get_tv_show_rating_and_review_by_grade(
                    grade
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_rating_and_review_by_tv_show_id(tv_show_id: str):
        """Get tv_show_rating_and_review by tv_show_id"""
        try:
            with SessionLocal() as db:
                tv_show_rating_and_review_repository = TVShowRatingAndReviewRepository(
                    db
                )
                return tv_show_rating_and_review_repository.get_tv_show_rating_and_review_by_tv_show_id(
                    tv_show_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_tv_show_rating_and_review_by_user_id(user_id: str):
        """Get tv_show_rating_and_review by user_id"""
        try:
            with SessionLocal() as db:
                tv_show_rating_and_review_repository = TVShowRatingAndReviewRepository(
                    db
                )
                return tv_show_rating_and_review_repository.get_tv_show_rating_and_review_by_user_id(
                    user_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_tv_shows_ratings_and_reviews():
        """Get all tv_shows_ratings_and_reviews"""
        try:
            with SessionLocal() as db:
                tv_shows_ratings_and_reviews_repository = (
                    TVShowRatingAndReviewRepository(db)
                )
                return (
                    tv_shows_ratings_and_reviews_repository.get_all_tv_shows_ratings_and_reviews()
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_tv_show_rating_and_review_by_id(tv_show_rating_and_review_id: str):
        """Delete tv_show_rating_and_review by id"""
        try:
            with SessionLocal() as db:
                tv_show_rating_and_review_repository = TVShowRatingAndReviewRepository(
                    db
                )
                return tv_show_rating_and_review_repository.delete_tv_show_rating_and_review_by_id(
                    tv_show_rating_and_review_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def update_tv_show_rating_and_review_comment(
        tv_show_rating_and_review_id: str, comment: str
    ):
        """Update tv_show_rating_and_review comment section"""
        try:
            with SessionLocal() as db:
                tv_show_rating_and_review_repository = TVShowRatingAndReviewRepository(
                    db
                )
                return tv_show_rating_and_review_repository.update_tv_show_rating_and_review_comment(
                    tv_show_rating_and_review_id, comment
                )
        except Exception as e:
            raise e from e
