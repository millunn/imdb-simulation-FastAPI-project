import uuid
from app.db.database import SessionLocal
from app.genres.exceptions import GenreNotFoundException
from app.genres.repository import GenreRepository
from app.languages.exceptions import LanguageNotFoundException
from app.languages.repository import LanguageRepository
from app.tv_shows_and_series.repository import TVShowRepository


class TvShowServices:
    @staticmethod
    def create_tv_show(
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
            with SessionLocal() as db:
                language_repository = LanguageRepository(db)
                language = language_repository.get_language_by_name(language_name)
                if language is None:
                    raise LanguageNotFoundException(
                        message=f"Language with provided name: {language_name} not found.",
                        code=400,
                    )
                genre_repository = GenreRepository(db)
                genre = genre_repository.get_genre_by_category(genre_category)
                if genre is None:
                    raise GenreNotFoundException(
                        message=f"Genre with provided category: {genre_category} not found.",
                        code=400,
                    )
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.create_tv_show(
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
        except Exception as e:
            raise e

    @staticmethod
    def get_tv_show_by_id(tv_show_id: str):
        try:
            uuid.UUID(str(tv_show_id))
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_id(tv_show_id)
        except ValueError:
            raise Exception(f"Provided id: {tv_show_id} not uuid")
        except Exception as e:
            raise e

    @staticmethod
    def get_tv_show_by_title(title: str):
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_title(title)
        except Exception as e:
            raise e

    @staticmethod
    def get_tv_show_by_language(language: str):
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_language(language)
        except Exception as e:
            raise e

    @staticmethod
    def get_tv_show_by_genre(genre: str):
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_genre(genre)
        except Exception as e:
            raise e

    @staticmethod
    def get_tv_show_by_release_year(release_year: str):
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_tv_show_by_release_year(release_year)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_tv_shows():
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.get_all_tv_shows()
        except Exception as e:
            raise e

    @staticmethod
    def delete_tv_show_by_id(tv_show_id: str):
        try:
            with SessionLocal() as db:
                tv_show_repository = TVShowRepository(db)
                return tv_show_repository.delete_tv_show_by_id(tv_show_id)
        except Exception as e:
            raise e
