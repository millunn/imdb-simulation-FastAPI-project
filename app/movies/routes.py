from fastapi import APIRouter, Depends
from app.movies.controller import MovieController
from app.movies.schemas import MovieSchema, MovieSchemaSchemaIn

from app.users.controller.user_auth_controller import JWTBearer

movie_router = APIRouter(tags=["movies"], prefix="/api/movie")


# superuser
@movie_router.post(
    "/add-new-movie",
    response_model=MovieSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def create_movie(movie: MovieSchemaSchemaIn):
    return MovieController.create_movie(
        movie.title,
        movie.plot,
        movie.duration,
        movie.release_year,
        movie.director,
        movie.writer,
        movie.producer,
        movie.synopsis,
    )


@movie_router.get("/id", response_model=MovieSchema)
def get_movie_by_id(movie_id: str):
    return MovieController.get_movie_by_id(movie_id)


@movie_router.get("/title", response_model=list[MovieSchema])
def get_movie_by_name(title: str):
    return MovieController.get_movie_by_name(title)


@movie_router.get("/get-all-movies", response_model=list[MovieSchema])
def get_all_movies():
    return MovieController.get_all_movies()


# superuser
@movie_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_movie_by_id(movie_id: str):
    return MovieController.delete_movie_by_id(movie_id)
