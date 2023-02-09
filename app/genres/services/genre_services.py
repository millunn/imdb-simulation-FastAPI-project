from app.db.database import SessionLocal
from app.genres.repository import GenreRepository


class GenreServices:
    @staticmethod
    def create_genre(category, description):
        with SessionLocal() as db:
            try:
                genre_repository = GenreRepository(db)
                return genre_repository.create_genre(category, description)
            except Exception as e:
                raise e

    @staticmethod
    def get_genre_by_id(genre_id: str):
        with SessionLocal() as db:
            genre_repository = GenreRepository(db)
            return genre_repository.get_genre_by_id(genre_id)

    @staticmethod
    def get_genre_by_category(category: str):
        with SessionLocal() as db:
            genre_repository = GenreRepository(db)
            return genre_repository.get_genre_by_category(category)

    @staticmethod
    def get_all_genres():
        with SessionLocal() as db:
            genre_repository = GenreRepository(db)
            return genre_repository.get_all_genres()

    @staticmethod
    def delete_genre_by_id(genre_id: str):
        try:
            with SessionLocal() as db:
                genre_repository = GenreRepository(db)
                return genre_repository.delete_genre_by_id(genre_id)
        except Exception as e:
            raise e
