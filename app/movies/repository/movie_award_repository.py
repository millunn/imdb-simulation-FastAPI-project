""" MovieAward Repository module """

from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.awards.exceptions import AwardNotFoundException
from app.movies.exceptions import MovieNotFoundException
from app.movies.exceptions import MovieAwardNotFoundException
from app.movies.models import MovieAward


class MovieAwardRepository:
    """MovieAward model repository"""

    def __init__(self, db: Session):
        self.db = db

    def create_movie_award(self, movie_id, award_id):
        """Create new movie_award"""
        try:
            movie_award = MovieAward(movie_id, award_id)
            self.db.add(movie_award)
            self.db.commit()
            self.db.refresh(movie_award)
            return movie_award
        except IntegrityError as e:
            raise e from e

    def get_movie_by_award_id(self, award_id: str):
        """Get movie by award_id"""
        movie_by_award_id = (
            self.db.query(MovieAward).filter(MovieAward.award_id == award_id).all()
        )
        if (movie_by_award_id is None) or (movie_by_award_id == []):
            raise MovieNotFoundException(
                message=f"Movie with provided award id: {award_id} not found",
                code=400,
            )
        return movie_by_award_id

    def get_award_by_movie_id(self, movie_id: str):
        """Get award by movie_id"""
        award_by_movie_id = (
            self.db.query(MovieAward).filter(MovieAward.movie_id == movie_id).all()
        )
        if (award_by_movie_id is None) or (award_by_movie_id == []):
            raise AwardNotFoundException(
                message=f"Award with provided movie id: {movie_id} not found",
                code=400,
            )
        return award_by_movie_id

    def get_all_movies_with_all_awards(self):
        """Get all movies with all awards"""
        movie_award = self.db.query(MovieAward).all()
        if (movie_award is None) or (movie_award == []):
            raise AwardNotFoundException(
                message=f"The list is empty!",
                code=400,
            )
        return movie_award

    def get_top_five_most_awarded_movies(self):
        """Get top five most awarded movies"""
        movie_rating_and_review = (
            self.db.query(MovieAward)
            .group_by(MovieAward.movie_id)
            .order_by(desc("number_of_awards"))
            .limit(5)
            .values(
                MovieAward.movie_id.label("movie_id"),
                func.count(MovieAward.award_id).label("number_of_awards"),
            )
        )
        return movie_rating_and_review

    def delete_movie_award_by_id(self, movie_award_id: str):
        """Delete a pair movie_award by id"""
        try:
            movie_award = (
                self.db.query(MovieAward)
                .filter(MovieAward.id == movie_award_id)
                .first()
            )
            if movie_award is None:
                raise MovieAwardNotFoundException(
                    code=400,
                    message=f"Pair with provided id: {movie_award_id} not found.",
                )
            self.db.delete(movie_award)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e
