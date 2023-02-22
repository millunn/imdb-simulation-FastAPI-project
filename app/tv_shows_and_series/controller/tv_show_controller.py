from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.genres.exceptions import GenreNotFoundException
from app.languages.exceptions import LanguageNotFoundException
from app.tv_shows_and_series.exceptions import (
    TVShowEpisodeDurationException,
    TVShowNotFoundException,
    TVShowReleaseYearDigitException,
    TVShowReleaseYearLenghtException,
)
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
        except TVShowEpisodeDurationException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except TVShowReleaseYearDigitException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except TVShowReleaseYearLenghtException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except LanguageNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except GenreNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail="Tv show with provided data already exists.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_by_id(tv_show_id: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_id(tv_show_id)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_by_title(title: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_title(title)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_by_language(language: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_language(language)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_by_genre(genre: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_genre(genre)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_tv_show_by_release_year(release_year: str):
        try:
            tv_show = TVShowServices.get_tv_show_by_release_year(release_year)
            return tv_show
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_tv_shows():
        try:
            tv_shows = TVShowServices.get_all_tv_shows()
            return tv_shows
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

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
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_tv_show_by_title_decs():
        try:
            order_by_title_desc = TVShowServices.order_tv_show_by_title_decs()
            return order_by_title_desc
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_tv_show_by_title_asc():
        try:
            order_by_title_asc = TVShowServices.order_tv_show_by_title_asc()
            return order_by_title_asc
        except TVShowNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_top_five_tv_shows_by_ratings():
        try:
            tv_shows = TVShowServices.get_top_five_tv_shows_by_ratings()
            return tv_shows
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_five_most_rated_tv_shows():
        try:
            tv_shows = TVShowServices.get_five_most_rated_tv_shows()
            return tv_shows
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_genre_statistics():
        try:
            tv_shows = TVShowServices.get_genre_statistics()
            return tv_shows
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_language_statistics():
        try:
            tv_shows = TVShowServices.get_language_statistics()
            return tv_shows
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
