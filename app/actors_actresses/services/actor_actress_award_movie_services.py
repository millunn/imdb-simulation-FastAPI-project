""" Actor/Actress-Award-Movie Services module """

from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.repository import (
    ActorActressAwardMovieRepository,
    ActorActressRepository,
)
from app.awards.exceptions.award_exceptions import AwardNotFoundException
from app.awards.repository import AwardRepository
from app.db.database import SessionLocal
from app.movies.exceptions import MovieNotFoundException
from app.movies.repository import MovieRepository


class ActorActressAwardMovieServices:
    """Actor/Actress-Award-Movie model services"""

    @staticmethod
    def create_actor_actress_award_movie(actor_actress_id, award_id, movie_id):
        """Create new actor_actress_award_movie"""
        try:
            with SessionLocal() as db:
                actor_actress_repository = ActorActressRepository(db)
                actor_actress = actor_actress_repository.get_actor_actress_by_id(
                    actor_actress_id
                )
                if actor_actress is None:
                    raise ActorActressNotFoundException(
                        message=f"Actor/actress with provided id: {actor_actress_id} not found.",
                        code=400,
                    )
                award_repository = AwardRepository(db)
                award = award_repository.get_award_by_id(award_id)
                if award is None:
                    raise AwardNotFoundException(
                        message=f"Award with provided id: {award_id} not found.",
                        code=400,
                    )
                actor_actress_award_movie_repository = ActorActressAwardMovieRepository(
                    db
                )
                movie_repository = MovieRepository(db)
                movie = movie_repository.get_movie_by_id(movie_id)
                if movie is None:
                    raise MovieNotFoundException(
                        message=f"Movie with provided id: {movie_id} not found.",
                        code=400,
                    )
                return actor_actress_award_movie_repository.create_actor_actress_award_movie(
                    actor_actress_id,
                    award_id,
                    movie_id,
                )
        except IntegrityError as e:
            raise e from e
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        """Get award by actor_actress_id"""
        try:
            with SessionLocal() as db:
                award_actor_actress_repository = ActorActressAwardMovieRepository(db)
                return award_actor_actress_repository.get_award_by_actor_actress_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_award_by_movie_id(movie_id: str):
        """Get award by movie_id"""
        try:
            with SessionLocal() as db:
                award_movie_repository = ActorActressAwardMovieRepository(db)
                return award_movie_repository.get_award_by_movie_id(movie_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        """Get actor_actress by award_id"""
        try:
            with SessionLocal() as db:
                actor_actress_award_movie_repository = ActorActressAwardMovieRepository(
                    db
                )
                return (
                    actor_actress_award_movie_repository.get_actor_actress_by_award_id(
                        award_id
                    )
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_actor_actress_by_movie_id(movie_id: str):
        """Get actor_actress by movie_id"""
        try:
            with SessionLocal() as db:
                actor_actress_movie_repository = ActorActressAwardMovieRepository(db)
                return actor_actress_movie_repository.get_actor_actress_by_movie_id(
                    movie_id
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_actors_actresses_with_all_awards_all_movies():
        """Get all actors_actresses with all awards and all movies"""
        try:
            with SessionLocal() as db:
                actor_actress_award_movie_repository = ActorActressAwardMovieRepository(
                    db
                )
                return (
                    actor_actress_award_movie_repository.get_all_actors_actresses_with_all_awards_all_movies()
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def get_top_five_most_awarded_movie_actors_actresses():
        """Get top five most awarded movie actors actresses"""
        try:
            with SessionLocal() as db:
                actor_actress_award_movie_repository = ActorActressAwardMovieRepository(
                    db
                )
                return (
                    actor_actress_award_movie_repository.get_top_five_most_awarded_movie_actors_actresses()
                )
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_actor_actress_award_movie_by_id(actor_actress_award_movie_id: str):
        """Delete a pair actor_actress_award_movie by id"""
        try:
            with SessionLocal() as db:
                actor_actress_award_movie_repository = ActorActressAwardMovieRepository(
                    db
                )
                return actor_actress_award_movie_repository.delete_actor_actress_award_movie_by_id(
                    actor_actress_award_movie_id
                )
        except Exception as e:
            raise e from e
