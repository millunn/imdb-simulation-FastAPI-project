""" Actor/Actress-Award-Movie Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.actors_actresses.exceptions import (
    ActorActressNotFoundException,
    ActorActressAwardMovieNotFoundException,
)

from app.actors_actresses.services import ActorActressAwardMovieServices
from app.awards.exceptions import AwardNotFoundException
from app.movies.exceptions import MovieNotFoundException


class ActorActressAwardMovieController:
    """Actor/Actress-Award-Movie model controller"""

    @staticmethod
    def create_actor_actress_award_movie(actor_actress_id, award_id, movie_id):
        """Create new actor_actress_award_movie"""
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
            ) from e
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except MovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail="Already in database") from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        """Get award by actor_actress_id"""
        try:
            award = ActorActressAwardMovieServices.get_award_by_actor_actress_id(
                actor_actress_id
            )
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_movie_id(movie_id: str):
        """Get award by movie_id"""
        try:
            award = ActorActressAwardMovieServices.get_award_by_movie_id(movie_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        """Get actor_actress by award_id"""
        try:
            actor_actress = (
                ActorActressAwardMovieServices.get_actor_actress_by_award_id(award_id)
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
    def get_actor_actress_by_movie_id(movie_id: str):
        """Get actor_actress by movie_id"""
        try:
            actor_actress = (
                ActorActressAwardMovieServices.get_actor_actress_by_movie_id(movie_id)
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
    def get_all_actors_actresses_with_all_awards_all_movies():
        """Get all actors_actresses with all awards and all movies"""
        try:
            actor_actress_award_movie = (
                ActorActressAwardMovieServices.get_all_actors_actresses_with_all_awards_all_movies()
            )
            return actor_actress_award_movie
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_top_five_most_awarded_movie_actors_actresses():
        """Get top five most awarded movie actors actresses"""
        try:
            actor_actress_award_movie = (
                ActorActressAwardMovieServices.get_top_five_most_awarded_movie_actors_actresses()
            )
            return actor_actress_award_movie
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_actor_actress_award_movie_by_id(actor_actress_award_movie_id: str):
        """Delete a pair actor_actress_award_movie by id"""
        try:
            ActorActressAwardMovieServices.delete_actor_actress_award_movie_by_id(
                actor_actress_award_movie_id
            )
            return Response(
                content=f"Pair with provided id - {actor_actress_award_movie_id} is deleted"
            )
        except ActorActressAwardMovieNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
