from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.genres.exceptions import GenreNotFoundException
from app.genres.services import GenreServices


class GenreController:
    @staticmethod
    def create_genre(category, description):
        try:
            genre = GenreServices.create_genre(category, description)
            return genre
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Genre with provided category - {category} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_genre_by_id(genre_id: str):
        try:
            genre = GenreServices.get_genre_by_id(genre_id)
            return genre
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_genre_by_category(category: str):
        try:
            genre = GenreServices.get_genre_by_category(category)
            return genre
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_genres():
        try:
            genres = GenreServices.get_all_genres()
            return genres
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_genre_by_id(genre_id: str):
        try:
            GenreServices.delete_genre_by_id(genre_id)
            return Response(content=f"Genre with provided id - {genre_id} is deleted")
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
