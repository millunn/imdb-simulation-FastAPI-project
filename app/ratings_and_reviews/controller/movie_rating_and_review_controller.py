from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.movies.exceptions import MovieNotFoundException
from app.ratings_and_reviews.exceptions import (
    MovieRatingAndReviewNotFoundException,
    MovieRatingAndReviewGradeException,
)
from app.ratings_and_reviews.services import MovieRatingAndReviewServices
from app.users.exceptions import UserNotFoundException


class MovieRatingAndReviewController:
    @staticmethod
    def create_movie_rating_and_review(grade, comment, movie_id, user_id):
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
            )
        except MovieNotFoundException as e:
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
                detail=f"Failed! The user with id: {user_id} has already reviewed movie with id: {movie_id}.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_rating_and_review_by_id(movie_rating_and_review_id: str):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_rating_and_review_by_grade(grade: int):
        try:
            movie_rating_and_review = (
                MovieRatingAndReviewServices.get_movie_rating_and_review_by_grade(grade)
            )
            return movie_rating_and_review
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_rating_and_review_by_movie_id(movie_id: str):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_movie_rating_and_review_by_user_id(user_id: str):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_movies_ratings_and_reviews():
        try:
            movies_ratings_and_reviews = (
                MovieRatingAndReviewServices.get_all_movies_ratings_and_reviews()
            )
            return movies_ratings_and_reviews
        except MovieRatingAndReviewNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_movie_rating_and_review_by_id(movie_rating_and_review_id: str):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_movie_rating_and_review_comment(
        movie_rating_and_review_id: str, comment: str
    ):
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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
