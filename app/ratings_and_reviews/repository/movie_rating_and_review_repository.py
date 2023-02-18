from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.ratings_and_reviews.exceptions import MovieRatingAndReviewNotFoundException
from app.ratings_and_reviews.models import MovieRatingAndReview


class MovieRatingAndReviewRepository:
    def __init__(self, db: Session):
        self.db = db

    # superuser
    def create_movie_rating_and_review(self, grade, comment, movie_id, user_id):
        try:
            movie_rating_and_review = MovieRatingAndReview(
                grade, comment, movie_id, user_id
            )
            self.db.add(movie_rating_and_review)
            self.db.commit()
            self.db.refresh(movie_rating_and_review)
            return movie_rating_and_review
        except IntegrityError as e:
            raise e

    # superuser
    def get_movie_rating_and_review_by_id(self, movie_rating_and_review_id: str):
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
        movies_ratings_and_reviews = self.db.query(MovieRatingAndReview).all()
        return movies_ratings_and_reviews

    # superuser
    def delete_movie_rating_and_review_by_id(self, movie_rating_and_review_id: str):
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
            raise e
