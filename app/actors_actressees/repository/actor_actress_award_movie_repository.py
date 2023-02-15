from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.actors_actressees.exceptions import ActorActressNotFoundException
from app.actors_actressees.models import ActorActressAwardMovie
from app.awards.exceptions import AwardNotFoundException


class ActorActressAwardMovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_actor_actress_award_movie(self, actor_actress_id, award_id, movie_id):
        try:
            actor_actress_award_movie = ActorActressAwardMovie(
                actor_actress_id, award_id, movie_id
            )
            self.db.add(actor_actress_award_movie)
            self.db.commit()
            self.db.refresh(actor_actress_award_movie)
            return actor_actress_award_movie
        except IntegrityError as e:
            raise e

    def get_award_by_actor_actress_id(self, actor_actress_id: str):
        award_by_actor_actress_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.actor_actress_id == actor_actress_id)
            .all()
        )
        print(award_by_actor_actress_id)
        if award_by_actor_actress_id is None:
            raise AwardNotFoundException(
                message=f"Award with provided actor/actress id: {actor_actress_id} not found",
                code=400,
            )
        return award_by_actor_actress_id

    def get_award_by_movie_id(self, movie_id: str):
        award_by_movie_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.movie_id == movie_id)
            .all()
        )
        if award_by_movie_id is None:
            raise AwardNotFoundException(
                message=f"Award with provided movie id: {movie_id} not found",
                code=400,
            )
        return award_by_movie_id

    def get_actor_actress_by_award_id(self, award_id: str):
        actor_actress_by_award_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.award_id == award_id)
            .all()
        )
        if actor_actress_by_award_id is None:
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided award id: {award_id} not found",
                code=400,
            )
        return actor_actress_by_award_id

    def get_actor_actress_by_movie_id(self, movie_id: str):
        actor_actress_by_movie_id = (
            self.db.query(ActorActressAwardMovie)
            .filter(ActorActressAwardMovie.movie_id == movie_id)
            .all()
        )
        if actor_actress_by_movie_id is None:
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided movie id: {movie_id} not found",
                code=400,
            )
        return actor_actress_by_movie_id

    def get_all_actor_actress_with_all_awards_all_movies(self):
        actor_actress_award_movie = self.db.query(ActorActressAwardMovie).all()
        return actor_actress_award_movie
