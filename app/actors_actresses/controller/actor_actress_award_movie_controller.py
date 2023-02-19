from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.services import ActorActressAwardMovieServices
from app.awards.exceptions import AwardNotFoundException
from app.movies.exceptions import MovieNotFoundException


class ActorActressAwardMovieController:
    @staticmethod
    def create_actor_actress_award_movie(actor_actress_id, award_id, movie_id):
        try:
            actor_actress_award_movie = (
                ActorActressAwardMovieServices.create_actor_actress_award_movie(
                    actor_actress_id,
                    award_id,
                    movie_id,
                )
            )
            return actor_actress_award_movie
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        try:
            award = ActorActressAwardMovieServices.get_award_by_actor_actress_id(
                actor_actress_id
            )
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_movie_id(movie_id: str):
        try:
            award = ActorActressAwardMovieServices.get_award_by_movie_id(movie_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        try:
            actor_actress = (
                ActorActressAwardMovieServices.get_actor_actress_by_award_id(award_id)
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
    def get_actor_actress_by_movie_id(movie_id: str):
        try:
            actor_actress = (
                ActorActressAwardMovieServices.get_actor_actress_by_movie_id(movie_id)
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
    def get_all_actor_actress_with_all_awards_all_movies():
        try:
            actor_actress_award_movie = (
                ActorActressAwardMovieServices.get_all_actor_actress_with_all_awards_all_movies()
            )
            return actor_actress_award_movie
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_top_five_most_awarded_movie_actors_actresses():
        try:
            actor_actress_award_movie = (
                ActorActressAwardMovieServices.get_top_five_most_awarded_movie_actors_actresses()
            )
            return actor_actress_award_movie
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
