from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.genres.exceptions import GenreNotFoundException

from app.genres.models import Genre


class GenreRepository:
    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_genre(self, category, description):
        try:
            genre = Genre(category, description)
            self.db.add(genre)
            self.db.commit()
            self.db.refresh(genre)
            return genre
        except IntegrityError as e:
            raise e

    def get_genre_by_id(self, genre_id: str):
        genre = self.db.query(Genre).filter(Genre.id == genre_id).first()
        if genre is None:
            raise GenreNotFoundException(
                f"Genre with provided id: {genre_id} not found.", 400
            )
        return genre

    def get_genre_by_category(self, category: str):
        genre = self.db.query(Genre).filter(Genre.category.ilike(f"%{category}%")).all()
        if (genre is None) or (genre == []):
            raise GenreNotFoundException(
                f"Genre with provided category: {category} not found.", 400
            )
        return genre

    def get_all_genres(self):
        genres = self.db.query(Genre).all()
        return genres

    ##superuser
    def delete_genre_by_id(self, genre_id: str):
        try:
            genre = self.db.query(Genre).filter(Genre.id == genre_id).first()
            if genre is None:
                raise GenreNotFoundException(
                    f"Genre with provided id: {genre_id} not found.", 400
                )
            self.db.delete(genre)
            self.db.commit()
            return True
        except Exception as e:
            raise e
