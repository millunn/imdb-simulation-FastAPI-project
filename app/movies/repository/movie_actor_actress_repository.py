""" Movie-ActorActress Repository module """

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.models.actor_actress import ActorActress
from app.movies.exceptions import (
    MovieNotFoundException,
    MovieActorActressNotFoundException,
)
from app.movies.models import MovieActorActress


class MovieActorActressRepository:
    """Movie-ActorActress model repository"""

    def __init__(self, db: Session):
        self.db = db

    def create_movie_actor_actress(self, movie_id, actor_actress_id):
        """Create new movie_actor_actress pair"""
        try:
            movie_actor_actress = MovieActorActress(movie_id, actor_actress_id)
            self.db.add(movie_actor_actress)
            self.db.commit()
            self.db.refresh(movie_actor_actress)
            return movie_actor_actress
        except IntegrityError as e:
            raise e from e

    def get_movie_by_actor_actress_id(self, actor_actress_id: str):
        """Get movie by actor_actress_id"""
        movie_by_actor_actress_id = (
            self.db.query(MovieActorActress)
            .filter(MovieActorActress.actor_actress_id == actor_actress_id)
            .all()
        )
        if (movie_by_actor_actress_id is None) or (movie_by_actor_actress_id == []):
            raise MovieNotFoundException(
                message=f"Movie with provided actor/actress id: {actor_actress_id} not found",
                code=400,
            )
        return movie_by_actor_actress_id

    def get_actor_actress_by_movie_id(self, movie_id: str):
        """Get actor_actress by movie_id"""
        actor_actress_by_movie_id = (
            self.db.query(MovieActorActress)
            .filter(MovieActorActress.movie_id == movie_id)
            .all()
        )
        if (actor_actress_by_movie_id is None) or (actor_actress_by_movie_id == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided movie id: {movie_id} not found",
                code=400,
            )
        return actor_actress_by_movie_id

    def get_all_movies_with_all_actors_actresses(self):
        """Get all movies with all actors_actresses"""
        movie_actor_actress = self.db.query(MovieActorActress).all()
        if (movie_actor_actress is None) or (movie_actor_actress == []):
            raise ActorActressNotFoundException(
                message=f"The list is empty!",
                code=400,
            )
        return movie_actor_actress

    def get_actors_by_movie_id(self, movie_id: str):
        """Get actors by movie_id"""
        actors_by_movie_id = (
            self.db.query(ActorActress)
            .join(
                MovieActorActress, ActorActress.id == MovieActorActress.actor_actress_id
            )
            .filter(ActorActress.gender == "m", MovieActorActress.movie_id == movie_id)
            .all()
        )
        if (actors_by_movie_id is None) or (actors_by_movie_id == []):
            raise ActorActressNotFoundException(
                message=f"Actors with provided movie id: {movie_id} not found",
                code=400,
            )
        return actors_by_movie_id

    def get_actresses_by_movie_id(self, movie_id: str):
        """Get actresses by movie_id"""
        actresses_by_movie_id = (
            self.db.query(ActorActress)
            .join(
                MovieActorActress, ActorActress.id == MovieActorActress.actor_actress_id
            )
            .filter(ActorActress.gender == "f", MovieActorActress.movie_id == movie_id)
            .all()
        )
        if (actresses_by_movie_id is None) or (actresses_by_movie_id == []):
            raise ActorActressNotFoundException(
                message=f"Actresses with provided movie id: {movie_id} not found",
                code=400,
            )
        return actresses_by_movie_id

    def delete_movie_actor_actress_by_id(self, movie_actor_actress_id: str):
        """Delete a pair actor_actress_movie by id"""
        try:
            movie_actor_actress = (
                self.db.query(MovieActorActress)
                .filter(MovieActorActress.id == movie_actor_actress_id)
                .first()
            )
            if movie_actor_actress is None:
                raise MovieActorActressNotFoundException(
                    code=400,
                    message=f"Pair with provided id: {movie_actor_actress_id} not found.",
                )
            self.db.delete(movie_actor_actress)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e
