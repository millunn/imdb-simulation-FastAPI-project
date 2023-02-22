import uuid

from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.repository import ActorActressRepository
from app.db.database import SessionLocal
from app.movies.exceptions import MovieNotFoundException
from app.movies.repository import MovieActorActressRepository, MovieRepository


class MovieActorActressServices:
    @staticmethod
    def create_movie_actor_actress(movie_id, actor_actress_id):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                movie = movie_repository.get_movie_by_id(movie_id)
                if movie is None:
                    raise MovieNotFoundException(
                        message=f"Movie with provided id: {movie_id} not found.",
                        code=400,
                    )
                actor_actress_repository = ActorActressRepository(db)
                actor_actress = actor_actress_repository.get_actor_actress_by_id(
                    actor_actress_id
                )
                if actor_actress is None:
                    raise ActorActressNotFoundException(
                        message=f"Actor/actress with provided id: {actor_actress_id} not found.",
                        code=400,
                    )
                movie_actor_actress_repository = MovieActorActressRepository(db)
                return movie_actor_actress_repository.create_movie_actor_actress(
                    movie_id, actor_actress_id
                )
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_actor_actress_id(actor_actress_id: str):
        try:
            with SessionLocal() as db:
                award_actor_actress_repository = MovieActorActressRepository(db)
                return award_actor_actress_repository.get_movie_by_actor_actress_id(
                    actor_actress_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_actor_actress_by_movie_id(movie_id: str):
        try:
            with SessionLocal() as db:
                actor_actress_movie_repository = MovieActorActressRepository(db)
                return actor_actress_movie_repository.get_actor_actress_by_movie_id(
                    movie_id
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_all_movies_with_all_actors_actresses():
        try:
            with SessionLocal() as db:
                movie_actor_actress_repository = MovieActorActressRepository(db)
                return (
                    movie_actor_actress_repository.get_all_movies_with_all_actors_actresses()
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_actors_by_movie_id(movie_id: str):
        try:
            with SessionLocal() as db:
                actor_movie_repository = MovieActorActressRepository(db)
                return actor_movie_repository.get_actors_by_movie_id(movie_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_actresses_by_movie_id(movie_id: str):
        try:
            with SessionLocal() as db:
                actress_movie_repository = MovieActorActressRepository(db)
                return actress_movie_repository.get_actresses_by_movie_id(movie_id)
        except Exception as e:
            raise e
