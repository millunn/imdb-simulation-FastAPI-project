from app.db.database import SessionLocal
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
        language_id,
        genre_id,
    ):
        try:
            with SessionLocal() as db:
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
                    language_id,
                    genre_id,
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
