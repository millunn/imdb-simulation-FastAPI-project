from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, String


class TvShowActorActress(Base):
    __tablename__ = "tv_show_actor_actress"
    tv_show_id = Column(String(50), ForeignKey("tv_shows_and_series.id"))
    tv_show = relationship("TVShow", lazy="subquery")

    actor_actress_id = Column(String(50), ForeignKey("actors_actresses.id"))
    actor_actress = relationship("ActorActress", lazy="subquery")

    __table_args__ = (PrimaryKeyConstraint("tv_show_id", "actor_actress_id"),)

    def __init__(self, tv_show_id, actor_actress_id):
        self.tv_show_id = tv_show_id
        self.actor_actress_id = actor_actress_id
