from fastapi import HTTPException, Response

from app.genres.services import GenreServices


class GenreController:
    @staticmethod
    def create_genre(category, description):
        try:
            genre = GenreServices.create_genre(category, description)
            return genre
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_genre_by_id(genre_id: str):
        genre = GenreServices.get_genre_by_id(genre_id)
        if genre:
            return genre
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Genre with provided id {genre_id} does not exist",
            )

    @staticmethod
    def get_genre_by_category(category: str):
        genre = GenreServices.get_genre_by_category(category)
        if genre:
            return genre
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Genre with provided category {category} does not exist",
            )

    @staticmethod
    def get_all_genres():
        genres = GenreServices.get_all_genres()
        return genres

    @staticmethod
    def delete_genre_by_id(genre_id: str):
        try:
            GenreServices.delete_genre_by_id(genre_id)
            return Response(content=f"Genre with provided id - {genre_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
