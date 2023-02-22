from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.movies.exceptions import (
    MovieNotFoundException,
    MovieActorActressNotFoundException,
)
from app.movies.services import MovieActorActressServices


class MovieActorActressController:
    @staticmethod
    def create_movie_actor_actress(movie_id, actor_actress_id):
        try:
            movie_actor_actress_award = (
                MovieActorActressServices.create_movie_actor_actress(
                    movie_id, actor_actress_id
                )
            )
            return movie_actor_actress_award

        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_movie_by_actor_actress_id(actor_actress_id: str):
        try:
            movie = MovieActorActressServices.get_movie_by_actor_actress_id(
                actor_actress_id
            )
            return movie
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_movie_id(movie_id: str):
        try:
            actor_actress = MovieActorActressServices.get_actor_actress_by_movie_id(
                movie_id
            )
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_movies_with_all_actors_actresses():
        try:
            movie_actor_actress_repository = (
                MovieActorActressServices.get_all_movies_with_all_actors_actresses()
            )
            return movie_actor_actress_repository
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actors_by_movie_id(movie_id: str):
        try:
            actor_actress = MovieActorActressServices.get_actors_by_movie_id(movie_id)
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actresses_by_movie_id(movie_id: str):
        try:
            actresses_by_movie_id = MovieActorActressServices.get_actresses_by_movie_id(
                movie_id
            )
            return actresses_by_movie_id
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_movie_actor_actress_by_id(movie_actor_actress_id: str):
        try:
            MovieActorActressServices.delete_movie_actor_actress_by_id(
                movie_actor_actress_id
            )
            return Response(
                content=f"Pair with provided id - {movie_actor_actress_id} is deleted"
            )
        except MovieActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
