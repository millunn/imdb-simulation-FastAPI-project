""" Actor/Actress-Award-Movie Repository module """

from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.actors_actresses.exceptions import (
    ActorActressNotFoundException,
    ActorActressAwardMovieNotFoundException,
)

from app.actors_actresses.models import ActorActressAwardMovie
from app.awards.exceptions import AwardNotFoundException


class ActorActressAwardMovieRepository:
    """Actor/Actress-Award-Movie model repository"""

    def __init__(self, db: Session):
        self.db = db

    def create_actor_actress_award_movie(self, actor_actress_id, award_id, movie_id):
        """Create new actor_actress_award_movie"""
        try:
            actor_actress_award_movie = ActorActressAwardMovie(
                actor_actress_id, award_id, movie_id
            )
            self.db.add(actor_actress_award_movie)
            self.db.commit()
            self.db.refresh(actor_actress_award_movie)
            return actor_actress_award_movie
        except IntegrityError as e:
            raise e from e

    def get_award_by_actor_actress_id(self, actor_actress_id: str):
        """Get award by actor_actress_id"""
        award_by_actor_actress_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.actor_actress_id == actor_actress_id)
            .all()
        )
        if (award_by_actor_actress_id is None) or (award_by_actor_actress_id == []):
            raise AwardNotFoundException(
                message=f"Award with provided actor/actress id: {actor_actress_id} not found",
                code=400,
            )
        return award_by_actor_actress_id

    def get_award_by_movie_id(self, movie_id: str):
        """Get award by movie_id"""
        award_by_movie_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.movie_id == movie_id)
            .all()
        )
        if (award_by_movie_id is None) or (award_by_movie_id == []):
            raise AwardNotFoundException(
                message=f"Award with provided movie id: {movie_id} not found",
                code=400,
            )
        return award_by_movie_id

    def get_actor_actress_by_award_id(self, award_id: str):
        """Get actor_actress by award_id"""
        actor_actress_by_award_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.award_id == award_id)
            .all()
        )
        if (actor_actress_by_award_id is None) or (actor_actress_by_award_id == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided award id: {award_id} not found",
                code=400,
            )
        return actor_actress_by_award_id

    def get_actor_actress_by_movie_id(self, movie_id: str):
        """Get actor_actress by movie_id"""
        actor_actress_by_movie_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.movie_id == movie_id)
            .all()
        )
        if (actor_actress_by_movie_id is None) or (actor_actress_by_movie_id == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided movie id: {movie_id} not found",
                code=400,
            )
        return actor_actress_by_movie_id

    def get_all_actors_actresses_with_all_awards_all_movies(self):
        """Get all actors_actresses with all awards and all movies"""
        actor_actress_award_movie = self.db.query(ActorActressAwardMovie).all()
        if (actor_actress_award_movie is None) or (actor_actress_award_movie == []):
            raise ActorActressNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return actor_actress_award_movie

    def get_top_five_most_awarded_movie_actors_actresses(self):
        """Get top five most awarded movie actors actresses"""
        actor_actress_award_movie = (
            self.db.query(ActorActressAwardMovie)
            .group_by(ActorActressAwardMovie.actor_actress_id)
            .order_by(desc("number_of_awards"))
            .limit(5)
            .values(
                ActorActressAwardMovie.actor_actress_id.label("actor_actress_id"),
                func.count(ActorActressAwardMovie.award_id).label("number_of_awards"),
            )
        )
        return actor_actress_award_movie

    def delete_actor_actress_award_movie_by_id(self, actor_actress_award_movie_id: str):
        """Delete a pair actor_actress_award_movie by id"""
        try:
            actor_actress_award_movie = (
                self.db.query(ActorActressAwardMovie)
                .filter(ActorActressAwardMovie.id == actor_actress_award_movie_id)
                .first()
            )
            if actor_actress_award_movie is None:
                raise ActorActressAwardMovieNotFoundException(
                    message=f"Pair with provided id: {actor_actress_award_movie_id} not found.",
                    code=400,
                )
            self.db.delete(actor_actress_award_movie)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e
