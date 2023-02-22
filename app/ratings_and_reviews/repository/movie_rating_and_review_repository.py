""" MovieRatingAndReview Repository module """

from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.ratings_and_reviews.exceptions import MovieRatingAndReviewNotFoundException
from app.ratings_and_reviews.models import MovieRatingAndReview


class MovieRatingAndReviewRepository:
    """MovieRatingAndReview model repository"""

    def __init__(self, db: Session):
        self.db = db

    # superuser
    def create_movie_rating_and_review(self, grade, comment, movie_id, user_id):
        """Create new movie_rating_and_review pair"""
        try:
            movie_rating_and_review = MovieRatingAndReview(
                grade, comment, movie_id, user_id
            )
            self.db.add(movie_rating_and_review)
            self.db.commit()
            self.db.refresh(movie_rating_and_review)
            return movie_rating_and_review
        except IntegrityError as e:
            raise e from e

    # superuser
    def get_movie_rating_and_review_by_id(self, movie_rating_and_review_id: str):
        """Get movie_rating_and_review by id"""
        movie_rating_and_review = (
            self.db.query(MovieRatingAndReview)
            .filter(MovieRatingAndReview.id == movie_rating_and_review_id)
            .first()
        )
        if movie_rating_and_review is None:
            raise MovieRatingAndReviewNotFoundException(
                message=f"Movie rating with provided id: {movie_rating_and_review_id} not found.",
                code=400,
            )
        return movie_rating_and_review

    def get_movie_rating_and_review_by_grade(self, grade: int):
        """Get movie_rating_and_review by grade"""
        movie_rating_and_review = (
            self.db.query(MovieRatingAndReview)
            .filter(MovieRatingAndReview.grade == grade)
            .all()
        )
        if (movie_rating_and_review is None) or (movie_rating_and_review == []):
            raise MovieRatingAndReviewNotFoundException(
                message=f"Movie ratings with provided grade: {grade} not found.",
                code=400,
            )
        return movie_rating_and_review

    def get_movie_rating_and_review_by_movie_id(self, movie_id: str):
        """Get movie_rating_and_review by movie_id"""
        movie_rating_and_review = (
            self.db.query(MovieRatingAndReview)
            .filter(MovieRatingAndReview.movie_id == movie_id)
            .all()
        )
        if (movie_rating_and_review is None) or (movie_rating_and_review == []):
            raise MovieRatingAndReviewNotFoundException(
                message=f"Movie ratings with provided movie id: {movie_id} not found.",
                code=400,
            )
        return movie_rating_and_review

    # superuser
    def get_movie_rating_and_review_by_user_id(self, user_id: str):
        """Get movie_rating_and_review by user_id"""
        movie_rating_and_review = (
            self.db.query(MovieRatingAndReview)
            .filter(MovieRatingAndReview.user_id == user_id)
            .all()
        )
        if (movie_rating_and_review is None) or (movie_rating_and_review == []):
            raise MovieRatingAndReviewNotFoundException(
                message=f"Movie ratings with provided user id: {user_id} not found.",
                code=400,
            )
        return movie_rating_and_review

    def get_all_movies_ratings_and_reviews(self):
        """Get all movies_ratings_and_reviews"""
        movies_ratings_and_reviews = self.db.query(MovieRatingAndReview).all()
        if (movies_ratings_and_reviews is None) or (movies_ratings_and_reviews == []):
            raise MovieRatingAndReviewNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return movies_ratings_and_reviews

    # superuser
    def delete_movie_rating_and_review_by_id(self, movie_rating_and_review_id: str):
        """Delete movie_rating_and_review by id"""
        try:
            movie_rating_and_review = (
                self.db.query(MovieRatingAndReview)
                .filter(MovieRatingAndReview.id == movie_rating_and_review_id)
                .first()
            )
            if movie_rating_and_review is None:
                raise MovieRatingAndReviewNotFoundException(
                    message=f"Movie rating with provided id: {movie_rating_and_review_id} not found.",
                    code=400,
                )
            self.db.delete(movie_rating_and_review)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e

    def update_movie_rating_and_review_comment(
        self, movie_rating_and_review_id: str, comment: str
    ):
        """Update movie_rating_and_review comment section"""
        try:
            movie_rating_and_review = (
                self.db.query(MovieRatingAndReview)
                .filter(MovieRatingAndReview.id == movie_rating_and_review_id)
                .first()
            )
            if movie_rating_and_review is None:
                raise MovieRatingAndReviewNotFoundException(
                    f"Movie rating with provided id: {movie_rating_and_review_id} not found.",
                    400,
                )
            movie_rating_and_review.comment = comment
            movie_rating_and_review.comment_date = datetime.strftime(
                datetime.now(), "%Y-%m-%d, %H:%M:%S"
            )
            self.db.add(movie_rating_and_review)
            self.db.commit()
            self.db.refresh(movie_rating_and_review)
            return movie_rating_and_review
        except Exception as e:
            raise e from e
