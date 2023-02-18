from app.db.database import SessionLocal
from app.movies.exceptions import (
    MovieNotFoundException,
)
from app.movies.repository import MovieRepository
from app.ratings_and_reviews.exceptions import MovieRatingAndReviewGradeException
from app.ratings_and_reviews.repository import MovieRatingAndReviewRepository
from app.users.exceptions import UserNotFoundException
from app.users.repository import UserRepository


class MovieRatingAndReviewServices:
    @staticmethod
    def create_movie_rating_and_review(grade, comment, movie_id, user_id):
        try:
            if 1 > grade or grade > 5:
                raise MovieRatingAndReviewGradeException(
                    message=f"Grade must be in range of 1 to 5.",
                    code=400,
                )
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                movie = movie_repository.get_movie_by_id(movie_id)
                if movie is None:
                    raise MovieNotFoundException(
                        message=f"Movie with provided movie id: {movie_id} not found.",
                        code=400,
                    )
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_id(user_id)
                if user is None:
                    raise UserNotFoundException(
                        message=f"User with provided user id: {user_id} not found.",
                        code=400,
                    )
                movie_rating_and_review_repository = MovieRatingAndReviewRepository(db)
                return (
                    movie_rating_and_review_repository.create_movie_rating_and_review(
                        grade, comment, movie_id, user_id
                    )
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_rating_and_review_by_id(movie_rating_and_review_id: str):
        try:
            with SessionLocal() as db:
                movie_rating_and_review_repository = MovieRatingAndReviewRepository(db)
                return movie_rating_and_review_repository.get_movie_rating_and_review_by_id(
                    movie_rating_and_review_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_rating_and_review_by_grade(grade: int):
        try:
            with SessionLocal() as db:
                movie_rating_and_review_repository = MovieRatingAndReviewRepository(db)
                return movie_rating_and_review_repository.get_movie_rating_and_review_by_grade(
                    grade
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_rating_and_review_by_movie_id(movie_id: str):
        try:
            with SessionLocal() as db:
                movie_rating_and_review_repository = MovieRatingAndReviewRepository(db)
                return movie_rating_and_review_repository.get_movie_rating_and_review_by_movie_id(
                    movie_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_rating_and_review_by_user_id(user_id: str):
        try:
            with SessionLocal() as db:
                movie_rating_and_review_repository = MovieRatingAndReviewRepository(db)
                return movie_rating_and_review_repository.get_movie_rating_and_review_by_user_id(
                    user_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_all_movies_ratings_and_reviews():
        try:
            with SessionLocal() as db:
                movies_ratings_and_reviews_repository = MovieRatingAndReviewRepository(
                    db
                )
                return (
                    movies_ratings_and_reviews_repository.get_all_movies_ratings_and_reviews()
                )
        except Exception as e:
            raise e

    @staticmethod
    def delete_movie_rating_and_review_by_id(movie_rating_and_review_id: str):
        try:
            with SessionLocal() as db:
                movie_rating_and_review_repository = MovieRatingAndReviewRepository(db)
                return movie_rating_and_review_repository.delete_movie_rating_and_review_by_id(
                    movie_rating_and_review_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def update_movie_rating_and_review_comment(
        movie_rating_and_review_id: str, comment: str
    ):
        try:
            with SessionLocal() as db:
                movie_rating_and_review_repository = MovieRatingAndReviewRepository(db)
                return movie_rating_and_review_repository.update_movie_rating_and_review_comment(
                    movie_rating_and_review_id, comment
                )
        except Exception as e:
            raise e
