""" MovieAward Services module """

from sqlalchemy.exc import IntegrityError

from app.awards.exceptions import AwardNotFoundException
from app.awards.repository.award_repository import AwardRepository
from app.db.database import SessionLocal
from app.movies.exceptions import MovieNotFoundException
from app.movies.repository import MovieAwardRepository, MovieRepository


class MovieAwardServices:
    """MovieAward model services"""

    @staticmethod
    def create_movie_award(movie_id, award_id):
        """Create new movie_award"""
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                movie = movie_repository.get_movie_by_id(movie_id)
                if movie is None:
                    raise MovieNotFoundException(
                        message=f"Movie with provided id: {movie_id} not found.",
                        code=400,
                    )
                award_repository = AwardRepository(db)
                award = award_repository.get_award_by_id(award_id)
                if award is None:
                    raise AwardNotFoundException(
                        message=f"Award with provided id: {award_id} not found.",
                        code=400,
                    )
                movie_award_repository = MovieAwardRepository(db)
                return movie_award_repository.create_movie_award(movie_id, award_id)
        except IntegrityError as e:
            raise e from e
        except Exception as e:
            raise e from e

    @staticmethod
    def get_movie_by_award_id(award_id: str):
        """Get movie by award_id"""
        try:
            with SessionLocal() as db:
                movie_award_repository = MovieAwardRepository(db)
                return movie_award_repository.get_movie_by_award_id(award_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_movie_id(movie_id: str):
        """Get award by movie_id"""
        try:
            with SessionLocal() as db:
                award_movie_repository = MovieAwardRepository(db)
                return award_movie_repository.get_award_by_movie_id(movie_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_movies_with_all_awards():
        """Get all movies with all awards"""
        try:
            with SessionLocal() as db:
                movie_award_repository = MovieAwardRepository(db)
                return movie_award_repository.get_all_movies_with_all_awards()
        except Exception as e:
            raise e from e

    @staticmethod
    def get_top_five_most_awarded_movies():
        """Get top five most awarded movies"""
        try:
            with SessionLocal() as db:
                movie_repository = MovieAwardRepository(db)
                return movie_repository.get_top_five_most_awarded_movies()
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_movie_award_by_id(movie_award_id: str):
        """Delete a pair movie_award by id"""
        try:
            with SessionLocal() as db:
                movie_award_repository = MovieAwardRepository(db)
                return movie_award_repository.delete_movie_award_by_id(movie_award_id)
        except Exception as e:
            raise e from e
