from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.genres.exceptions import GenreNotFoundException
from app.languages.exceptions import LanguageNotFoundException
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.services import TVShowServices


class TVShowController:
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
            tv_show = TVShowServices.create_tv_show(
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
            return tv_show
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Tv show with provided data already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_by_id(tv_show_id: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_id(tv_show_id)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_by_title(title: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_title(title)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_by_language(language: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_language(language)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_by_genre(genre: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_genre(genre)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_tv_show_by_release_year(release_year: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_release_year(release_year)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tv_shows():
        try:
            tv_shows = TVShowServices.get_all_tv_shows()
            return tv_shows
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_tv_show_by_id(tv_show_id: str):
        try:
            TVShowServices.delete_tv_show_by_id(tv_show_id)
            return Response(
                content=f"Tv show with provided id - {tv_show_id} is deleted"
            )
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))