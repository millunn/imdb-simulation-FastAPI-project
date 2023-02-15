from app.db.database import SessionLocal
from app.genres.exceptions import GenreNotFoundException
from app.genres.repository import GenreRepository
from app.languages.exceptions import LanguageNotFoundException
from app.languages.repository import LanguageRepository
from app.movies.repository import MovieRepository


class MovieServices:
    @staticmethod
    def create_movie(
        title,
        plot,
        duration,
        release_year,
        director,
        writer,
        producer,
        synopsis,
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
                movie_repository = MovieRepository(db)
                return movie_repository.create_movie(
                    title,
                    plot,
                    duration,
                    release_year,
                    director,
                    writer,
                    producer,
                    synopsis,
                    language_name,
                    genre_category,
                )
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_id(movie_id: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_id(movie_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_title(title: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_title(title)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_language(language: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_language(language)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_genre(genre: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_genre(genre)
        except Exception as e:
            raise e

    @staticmethod
    def get_movie_by_release_year(release_year: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_movie_by_release_year(release_year)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_movies():
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.get_all_movies()
        except Exception as e:
            raise e

    @staticmethod
    def delete_movie_by_id(movie_id: str):
        try:
            with SessionLocal() as db:
                movie_repository = MovieRepository(db)
                return movie_repository.delete_movie_by_id(movie_id)
        except Exception as e:
            raise e
