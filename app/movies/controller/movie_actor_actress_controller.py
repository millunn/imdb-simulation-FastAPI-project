from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.actors_actressees.exceptions import ActorActressNotFoundException
from app.movies.exceptions import MovieNotFoundException
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
            )
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )

        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

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
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_movies_with_all_actors_actresses():
        try:
            movie_actor_actress_repository = (
                MovieActorActressServices.get_all_movies_with_all_actors_actresses()
            )
            return movie_actor_actress_repository
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
