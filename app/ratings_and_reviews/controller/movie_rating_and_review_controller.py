""" MovieRatingAndReview Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.movies.exceptions import MovieNotFoundException
from app.ratings_and_reviews.exceptions import (
    MovieRatingAndReviewGradeException,
    MovieRatingAndReviewNotFoundException,
)
from app.ratings_and_reviews.services import MovieRatingAndReviewServices
from app.users.exceptions import UserNotFoundException


class MovieRatingAndReviewController:
    """MovieRatingAndReview model controller"""

    @staticmethod
    def create_movie_rating_and_review(grade, comment, movie_id, user_id):
        """Create new movie_rating_and_review pair"""
        try:
            movie_rating_and_review = (
                MovieRatingAndReviewServices.create_movie_rating_and_review(
                    grade, comment, movie_id, user_id
                )
            )
            return movie_rating_and_review
        except MovieRatingAndReviewGradeException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except MovieNotFoundException as e:
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
                detail=f"Failed! The user with id: {user_id} has already reviewed movie with id: {movie_id}.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_rating_and_review_by_id(movie_rating_and_review_id: str):
        """Get movie_rating_and_review by id"""
        try:
            movie_rating_and_review = (
                MovieRatingAndReviewServices.get_movie_rating_and_review_by_id(
                    movie_rating_and_review_id
                )
            )
            return movie_rating_and_review
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_rating_and_review_by_grade(grade: int):
        """Get movie_rating_and_review by grade"""
        try:
            movie_rating_and_review = (
                MovieRatingAndReviewServices.get_movie_rating_and_review_by_grade(grade)
            )
            return movie_rating_and_review
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_rating_and_review_by_movie_id(movie_id: str):
        """Get movie_rating_and_review by movie_id"""
        try:
            movie_rating_and_review = (
                MovieRatingAndReviewServices.get_movie_rating_and_review_by_movie_id(
                    movie_id
                )
            )
            return movie_rating_and_review
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_rating_and_review_by_user_id(user_id: str):
        """Get movie_rating_and_review by user_id"""
        try:
            movie_rating_and_review = (
                MovieRatingAndReviewServices.get_movie_rating_and_review_by_user_id(
                    user_id
                )
            )
            return movie_rating_and_review
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_movies_ratings_and_reviews():
        """Get all movies_ratings_and_reviews"""
        try:
            movies_ratings_and_reviews = (
                MovieRatingAndReviewServices.get_all_movies_ratings_and_reviews()
            )
            return movies_ratings_and_reviews
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_movie_rating_and_review_by_id(movie_rating_and_review_id: str):
        """Delete movie_rating_and_review by id"""
        try:
            MovieRatingAndReviewServices.delete_movie_rating_and_review_by_id(
                movie_rating_and_review_id
            )
            return Response(
                content=f"Movie rating with provided id - {movie_rating_and_review_id} is deleted"
            )
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_movie_rating_and_review_comment(
        movie_rating_and_review_id: str, comment: str
    ):
        """Update movie_rating_and_review comment section"""
        try:
            movie_rating_and_review = (
                MovieRatingAndReviewServices.update_movie_rating_and_review_comment(
                    movie_rating_and_review_id, comment
                )
            )
            return movie_rating_and_review
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
