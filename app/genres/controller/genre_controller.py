""" Genre Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.genres.exceptions import GenreNotFoundException
from app.genres.services import GenreServices


class GenreController:
    """Genre model controller"""

    @staticmethod
    def create_genre(category, description):
        """Create new genre"""
        try:
            genre = GenreServices.create_genre(category, description)
            return genre
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Genre with provided category - {category} already exists.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_genre_by_id(genre_id: str):
        """Get genre by id"""
        try:
            genre = GenreServices.get_genre_by_id(genre_id)
            return genre
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_genre_by_category(category: str):
        """Get genre by category"""
        try:
            genre = GenreServices.get_genre_by_category(category)
            return genre
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_genres():
        """Get all genres"""
        try:
            genres = GenreServices.get_all_genres()
            return genres
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_genre_by_id(genre_id: str):
        """Delete genre by id"""
        try:
            GenreServices.delete_genre_by_id(genre_id)
            return Response(content=f"Genre with provided id - {genre_id} is deleted")
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
