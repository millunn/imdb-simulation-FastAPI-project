import datetime
import pytest
import sqlalchemy
from sqlalchemy.exc import IntegrityError
from app.genres.repository import GenreRepository
from app.languages.repository import LanguageRepository
from app.tests import TestClass, TestingSessionLocal
from app.tv_shows_and_series.exceptions import TVShowNotFoundException
from app.tv_shows_and_series.exceptions import (
    TVShowReleaseYearDigitException,
    TVShowReleaseYearLenghtException,
)
from app.tv_shows_and_series.repository import TVShowRepository
from app.tv_shows_and_series.services import TVShowServices


class TestTVShowAndSerieRepo(TestClass):
    def create_language_for_methods(self):
        with TestingSessionLocal() as db:
            language_repository = LanguageRepository(db)
            language = language_repository.create_language("English", "EN")

    def create_genre_for_methods(self):
        with TestingSessionLocal() as db:
            genre_repository = GenreRepository(db)
            genre = genre_repository.create_genre("Comedy", "...")

    def create_tv_shows_for_methods(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men2",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men3",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men4",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )

    def test_create_tv_show(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            assert tv_show.title == "Two and half men"
            assert tv_show.plot == "..."
            assert tv_show.release_year == "1979"
            assert tv_show.creator == "Chuck Lorre"
            assert tv_show.seasons == 12
            assert tv_show.episodes == 21
            assert tv_show.episode_duration == datetime.time(0, 23)
            assert tv_show.language_name == "English"
            assert tv_show.genre_category == "Comedy"

    def test_create_tv_show_duplicate_error(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            with pytest.raises(IntegrityError) as e:
                tv_show1 = tv_show_repository.create_tv_show(
                    "Two and half men",
                    "...",
                    "1979",
                    "Chuck Lorre",
                    12,
                    21,
                    "00:23",
                    "English",
                    "Comedy",
                )

    def test_create_tv_show_language_not_found_error(self):
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            with pytest.raises(sqlalchemy.exc.IntegrityError) as e:
                tv_show = tv_show_repository.create_tv_show(
                    "Two and half men",
                    "...",
                    "1979",
                    "Chuck Lorre",
                    12,
                    21,
                    "00:23",
                    "English",
                    "Comedy",
                )

    def test_create_tv_show_genre_not_found_error(self):
        self.create_language_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            with pytest.raises(sqlalchemy.exc.IntegrityError) as e:
                tv_show = tv_show_repository.create_tv_show(
                    "Two and half men",
                    "...",
                    "1979",
                    "Chuck Lorre",
                    12,
                    21,
                    "00:23",
                    "English",
                    "Comedy",
                )

    def test_get_tv_show_by_id(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            tv_show1 = tv_show_repository.get_tv_show_by_id(tv_show.id)
            assert tv_show.title == tv_show1.title
            assert tv_show.plot == tv_show1.plot
            assert tv_show.release_year == tv_show1.release_year
            assert tv_show.creator == tv_show1.creator
            assert tv_show.seasons == tv_show1.seasons
            assert tv_show.episodes == tv_show1.episodes
            assert tv_show.episode_duration == tv_show1.episode_duration
            assert tv_show.language_name == tv_show1.language_name
            assert tv_show.genre_category == tv_show1.genre_category

    def test_get_tv_show_by_id_error_not_found(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            with pytest.raises(TVShowNotFoundException) as e:
                tv_show1 = tv_show_repository.get_tv_show_by_id("false_tv_show_id")

    def test_get_all_tv_shows(self):
        self.create_tv_shows_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            all_tv_shows = tv_show_repository.get_all_tv_shows()
            assert len(all_tv_shows) == 4

    def test_delete_tv_show_by_id(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            assert tv_show_repository.delete_tv_show_by_id(tv_show.id)

    def test_delete_tv_show_by_id_error_not_found(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            with pytest.raises(TVShowNotFoundException) as e:
                tv_show1 = tv_show_repository.delete_tv_show_by_id("false_tv_show_id")

    def get_tv_show_by_title(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            assert tv_show.title == "Two and half men"

    def test_get_tv_show_by_email_error_not_found(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            tv_show = tv_show_repository.create_tv_show(
                "Two and half men",
                "...",
                "1979",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
            with pytest.raises(TVShowNotFoundException) as e:
                tv_show = tv_show_repository.get_tv_show_by_title("false_title")

    def test_create_tv_show_title_integrity_error(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with TestingSessionLocal() as db:
            tv_show_repository = TVShowRepository(db)
            with pytest.raises(IntegrityError) as e:
                tv_show = tv_show_repository.create_tv_show(
                    None,
                    "...",
                    "1979",
                    "Chuck Lorre",
                    12,
                    21,
                    "00:23",
                    "English",
                    "Comedy",
                )

    def test_create_tv_show_release_year_not_integer_error(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with pytest.raises(TVShowReleaseYearDigitException) as e:
            tv_show = TVShowServices.create_tv_show(
                "Two and half men",
                "...",
                "dsadsdas",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )

    def test_create_tv_show_release_year_lenght_error(self):
        self.create_language_for_methods()
        self.create_genre_for_methods()
        with pytest.raises(TVShowReleaseYearLenghtException) as e:
            tv_show = TVShowServices.create_tv_show(
                "Two and half men",
                "...",
                "1999999",
                "Chuck Lorre",
                12,
                21,
                "00:23",
                "English",
                "Comedy",
            )
