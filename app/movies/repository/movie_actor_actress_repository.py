from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.movies.exceptions import MovieNotFoundException

from app.movies.models import MovieActorActress


class MovieActorActressRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_movie_actor_actress(self, movie_id, actor_actress_id):
        try:
            movie_actor_actress = MovieActorActress(movie_id, actor_actress_id)
            self.db.add(movie_actor_actress)
            self.db.commit()
            self.db.refresh(movie_actor_actress)
            return movie_actor_actress
        except IntegrityError as e:
            raise e

    def get_movie_by_actor_actress_id(self, actor_actress_id: str):
        movie_by_actor_actress_id = (
            self.db.query(MovieActorActress)
            .filter(MovieActorActress.actor_actress_id == actor_actress_id)
            .all()
        )
        if movie_by_actor_actress_id is None:
            raise MovieNotFoundException(
                message=f"Movie with provided actor/actress id: {actor_actress_id} not found",
                code=400,
            )
        return movie_by_actor_actress_id

    def get_actor_actress_by_movie_id(self, movie_id: str):
        actor_actress_by_movie_id = (
            self.db.query(MovieActorActress)
            .filter(MovieActorActress.movie_id == movie_id)
            .all()
        )
        if actor_actress_by_movie_id is None:
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided movie id: {movie_id} not found",
                code=400,
            )
        return actor_actress_by_movie_id

    def get_all_movies_with_all_actors_actresses(self):
        movie_actor_actress = self.db.query(MovieActorActress).all()
        return movie_actor_actress
