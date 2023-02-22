from uuid import uuid4
from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class TVShowAward(Base):
    __tablename__ = "tv_show_award"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    tv_show_id = Column(
        String(50), ForeignKey("tv_shows_and_series.id"), nullable=False
    )
    tv_show = relationship("TVShow", lazy="subquery")

    award_id = Column(String(50), ForeignKey("awards.id"), nullable=False)
    award = relationship("Award", lazy="subquery")

    __table_args__ = (
        UniqueConstraint("tv_show_id", "award_id", name="tv_show_award_uc"),
    )

    def __init__(self, tv_show_id, award_id):
        self.tv_show_id = tv_show_id
        self.award_id = award_id
