from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint


class ActorActressTvShow(Base):
    __tablename__ = "actor_actress_tv_show"
    tv_show_id = Column(String(50), ForeignKey("tv_shows_and_series.id"))
    tv_show = relationship("TVShowAndSerie", lazy="subquery")

    actor_actress_id = Column(String(50), ForeignKey("actors_actresses.id"))
    actor_actress = relationship("ActorActress", lazy="subquery")

    __table_args__ = (
        UniqueConstraint(
            "tv_show_id", "actor_actress_id", name="tv_show_actor_actress_uc"
        ),
    )

    def __init__(self, tv_show_id, actor_actress_id):
        self.tv_show_id = tv_show_id
        self.actor_actress_id = actor_actress_id
