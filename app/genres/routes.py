from fastapi import APIRouter, Depends

from app.genres.controller import GenreController
from app.genres.schemas.genre_schema import GenreSchema, GenreSchemaIn
from app.users.controller.user_auth_controller import JWTBearer

genre_router = APIRouter(tags=["genres"], prefix="/api/genres")


@genre_router.post(
    "/add-new-genre",
    response_model=GenreSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def create_genre(genre: GenreSchemaIn):
    return GenreController.create_genre(genre.category, genre.description)


@genre_router.get(
    "/id",
    response_model=GenreSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def get_genre_by_id(genre_id: str):
    return GenreController.get_genre_by_id(genre_id)


@genre_router.get("/category", response_model=list[GenreSchema])
def get_genre_by_category(category: str):
    return GenreController.get_genre_by_category(category)


@genre_router.get("/get-all-genres", response_model=list[GenreSchema])
def get_all_genres():
    return GenreController.get_all_genres()


@genre_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_genre_by_id(genre_id: str):
    return GenreController.delete_genre_by_id(genre_id)
