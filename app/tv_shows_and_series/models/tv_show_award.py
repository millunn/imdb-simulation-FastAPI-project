from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint


class TvShowAward(Base):
    __tablename__ = "tv_show_award"
    tv_show_id = Column(String(50), ForeignKey("tv_shows_and_series.id"))
    tv_show = relationship("TVShowAndSerie", lazy="subquery")

    award_id = Column(String(50), ForeignKey("awards.id"))
    award = relationship("Award", lazy="subquery")

    __table_args__ = (
        UniqueConstraint("tv_show_id", "award_id", name="tv_show_award_uc"),
    )

    def __init__(self, tv_show_id, award_id):
        self.tv_show_id = tv_show_id
        self.award_id = award_id
