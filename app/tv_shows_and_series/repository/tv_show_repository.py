from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.models import TVShow


class TVShowRepository:
    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_tv_show(
        self,
        title,
        plot,
        release_year,
        creator,
        seasons,
        episodes,
        episode_duration,
        language_name,
        genre_category,
    ):
        try:
            tv_show = TVShow(
                title,
                plot,
                release_year,
                creator,
                seasons,
                episodes,
                episode_duration,
                language_name,
                genre_category,
            )
            self.db.add(tv_show)
            self.db.commit()
            self.db.refresh(tv_show)
            return tv_show
        except IntegrityError as e:
            raise e

    def get_tv_show_by_id(self, tv_show_id: str):
        tv_show = self.db.query(TVShow).filter(TVShow.id == tv_show_id).first()
        if tv_show is None:
            raise TVShowNotFoundException(
                message=f"Tv show with provided id: {tv_show_id} not found.",
                code=400,
            )
        return tv_show

    # lista
    def get_tv_show_by_title(self, title: str):
        tv_show = self.db.query(TVShow).filter(TVShow.title.ilike(f"%{title}%")).all()
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided title: {title} not found.",
                code=400,
            )
        return tv_show

    # lista
    def get_tv_show_by_language(self, language: str):
        tv_show = (
            self.db.query(TVShow)
            .filter(TVShow.language_name.ilike(f"%{language}%"))
            .all()
        )
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided language: {language} not found.",
                code=400,
            )
        return tv_show

    # lista
    def get_tv_show_by_genre(self, genre: str):
        tv_show = (
            self.db.query(TVShow)
            .filter(TVShow.genre_category.ilike(f"%{genre}%"))
            .all()
        )
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided genre: {genre} not found.",
                code=400,
            )
        return tv_show

    # lista
    def get_tv_show_by_release_year(self, release_year: str):
        tv_show = (
            self.db.query(TVShow).filter(TVShow.release_year == release_year).all()
        )
        if (tv_show is None) or (tv_show == []):
            raise TVShowNotFoundException(
                message=f"Tv show with provided release_year: {release_year} not found.",
                code=400,
            )
        return tv_show

    def get_all_tv_shows(self):
        tv_shows = self.db.query(TVShow).all()
        return tv_shows

    ##superuser
    def delete_tv_show_by_id(self, tv_show_id: str):
        try:
            tv_show = self.db.query(TVShow).filter(TVShow.id == tv_show_id).first()
            if tv_show is None:
                raise TVShowNotFoundException(
                    message=f"Tv show with provided id: {tv_show_id} not found.",
                    code=400,
                )
            self.db.delete(tv_show)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def order_tv_show_by_title_decs(self):
        order_by_title_desc = self.db.query(TVShow).order_by(TVShow.title.desc()).all()
        return order_by_title_desc

    def order_tv_show_by_title_asc(self):
        order_by_title_asc = self.db.query(TVShow).order_by(TVShow.title.asc()).all()
        return order_by_title_asc
