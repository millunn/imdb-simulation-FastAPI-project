from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, String


class MovieActorActress(Base):
    __tablename__ = "movie_actor_actress"
    movie_id = Column(String(50), ForeignKey("movies.id"))
    movie = relationship("Movie", lazy="subquery")

    actor_actress_id = Column(String(50), ForeignKey("actors_actresses.id"))
    actor_actress = relationship("ActorActress", lazy="subquery")

    __table_args__ = (PrimaryKeyConstraint("movie_id", "actor_actress_id"),)

    def __init__(self, movie_id, actor_actress_id):
        self.movie_id = movie_id
        self.actor_actress_id = actor_actress_id
