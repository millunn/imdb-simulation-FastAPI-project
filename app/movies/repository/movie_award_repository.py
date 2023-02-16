from uuid import UUID, uuid4
import uuid
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.awards.exceptions import AwardNotFoundException
from app.movies.exceptions import MovieNotFoundException

from app.movies.models import MovieAward


class MovieAwardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_movie_award(self, movie_id, award_id):
        try:
            movie_award = MovieAward(movie_id, award_id)
            self.db.add(movie_award)
            self.db.commit()
            self.db.refresh(movie_award)
            return movie_award
        except IntegrityError as e:
            raise e

    def get_movie_by_award_id(self, award_id: str):
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
        movie_award = self.db.query(MovieAward).all()
        return movie_award
