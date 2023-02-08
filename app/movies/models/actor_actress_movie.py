from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint


class ActorActressMovie(Base):
    __tablename__ = "actor_actress_movie"
    movie_id = Column(String(50), ForeignKey("movies.id"))
    movie = relationship("Movie", lazy="subquery")

    actor_actress_id = Column(String(50), ForeignKey("actors_actresses.id"))
    actor_actress = relationship("ActorActress", lazy="subquery")

    __table_args__ = (
        UniqueConstraint("movie_id", "actor_actress_id", name="movie_actor_actress_uc"),
    )

    def __init__(self, movie_id, actor_actress_id):
        self.movie_id = movie_id
        self.actor_actress_id = actor_actress_id
