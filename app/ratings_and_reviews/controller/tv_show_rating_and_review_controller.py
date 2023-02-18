from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.ratings_and_reviews.exceptions import (
    TVShowRatingAndReviewNotFoundException,
    TVShowRatingAndReviewGradeException,
)
from app.ratings_and_reviews.services import TVShowRatingAndReviewServices
from app.users.exceptions import UserNotFoundException


class TVShowRatingAndReviewController:
    @staticmethod
    def create_tv_show_rating_and_review(grade, comment, tv_show_id, user_id):
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
            )
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Failed! The user with id: {user_id} has already reviewed tv show with id: {tv_show_id}.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_rating_and_review_by_id(tv_show_rating_and_review_id: str):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_rating_and_review_by_grade(grade: int):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_rating_and_review_by_tv_show_id(tv_show_id: str):
        try:
            tv_show_rating_and_review = TVShowRatingAndReviewServices.get_tv_show_rating_and_review_by_tv_show_id(
                tv_show_id
            )
            return tv_show_rating_and_review
        except TVShowRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_rating_and_review_by_user_id(user_id: str):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tv_shows_ratings_and_reviews():
        try:
            tv_shows_ratings_and_reviews = (
                TVShowRatingAndReviewServices.get_all_tv_shows_ratings_and_reviews()
            )
            return tv_shows_ratings_and_reviews
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_tv_show_rating_and_review_by_id(tv_show_rating_and_review_id: str):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_tv_show_rating_and_review_comment(
        tv_show_rating_and_review_id: str, comment: str
    ):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
