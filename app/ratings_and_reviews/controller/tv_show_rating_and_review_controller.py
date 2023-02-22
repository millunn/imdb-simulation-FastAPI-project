""" TVShowRatingAndReview Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.ratings_and_reviews.exceptions import (
    TVShowRatingAndReviewGradeException,
    TVShowRatingAndReviewNotFoundException,
)
from app.ratings_and_reviews.services import TVShowRatingAndReviewServices
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.users.exceptions import UserNotFoundException


class TVShowRatingAndReviewController:
    """TVShowRatingAndReview model controller"""

    @staticmethod
    def create_tv_show_rating_and_review(grade, comment, tv_show_id, user_id):
        """Create new tv_show_rating_and_review pair"""
        try:
            tv_show_rating_and_review = (
                TVShowRatingAndReviewServices.create_tv_show_rating_and_review(
                    grade, comment, tv_show_id, user_id
                )
            )
            return tv_show_rating_and_review
        except TVShowRatingAndReviewGradeException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Failed! The user with id: {user_id} has already reviewed tv show with id: {tv_show_id}.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_rating_and_review_by_id(tv_show_rating_and_review_id: str):
        """Get tv_show_rating_and_review by id"""
        try:
            tv_show_rating_and_review = (
                TVShowRatingAndReviewServices.get_tv_show_rating_and_review_by_id(
                    tv_show_rating_and_review_id
                )
            )
            return tv_show_rating_and_review
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_rating_and_review_by_grade(grade: int):
        """Get tv_show_rating_and_review by grade"""
        try:
            tv_show_rating_and_review = (
                TVShowRatingAndReviewServices.get_tv_show_rating_and_review_by_grade(
                    grade
                )
            )
            return tv_show_rating_and_review
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_rating_and_review_by_tv_show_id(tv_show_id: str):
        """Get tv_show_rating_and_review by tv_show_id"""
        try:
            tv_show_rating_and_review = TVShowRatingAndReviewServices.get_tv_show_rating_and_review_by_tv_show_id(
                tv_show_id
            )
            return tv_show_rating_and_review
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_rating_and_review_by_user_id(user_id: str):
        """Get tv_show_rating_and_review by user_id"""
        try:
            tv_show_rating_and_review = (
                TVShowRatingAndReviewServices.get_tv_show_rating_and_review_by_user_id(
                    user_id
                )
            )
            return tv_show_rating_and_review
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_tv_shows_ratings_and_reviews():
        """Get all tv_shows_ratings_and_reviews"""
        try:
            tv_shows_ratings_and_reviews = (
                TVShowRatingAndReviewServices.get_all_tv_shows_ratings_and_reviews()
            )
            return tv_shows_ratings_and_reviews
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_tv_show_rating_and_review_by_id(tv_show_rating_and_review_id: str):
        """Delete tv_show_rating_and_review by id"""
        try:
            TVShowRatingAndReviewServices.delete_tv_show_rating_and_review_by_id(
                tv_show_rating_and_review_id
            )
            return Response(
                content=f"Tv show rating with provided id - {tv_show_rating_and_review_id} is deleted"
            )
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_tv_show_rating_and_review_comment(
        tv_show_rating_and_review_id: str, comment: str
    ):
        """Update tv_show_rating_and_review comment section"""
        try:
            tv_show_rating_and_review = (
                TVShowRatingAndReviewServices.update_tv_show_rating_and_review_comment(
                    tv_show_rating_and_review_id, comment
                )
            )
            return tv_show_rating_and_review
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
