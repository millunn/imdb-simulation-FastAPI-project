from fastapi import APIRouter, Depends
from app.languages.controller import LanguageController
from app.languages.schemas import LanguageSchema, LanguageSchemaIn


from app.users.controller.user_auth_controller import JWTBearer

language_router = APIRouter(tags=["languages"], prefix="/api/languages")


@language_router.post(
    "/add-new-language",
    response_model=LanguageSchema,
    # dependencies=[Depends(JWTBearer("super_user"))],
)
def create_language(language: LanguageSchemaIn):
    return LanguageController.create_language(language.name, language.abbreviation)


@language_router.get("/id", response_model=LanguageSchema)
def get_language_by_id(language_id: str):
    return LanguageController.get_language_by_id(language_id)


@language_router.get("/name", response_model=LanguageSchema)
def get_language_by_name(name: str):
    return LanguageController.get_language_by_name(name)


@language_router.get("/abbreviation", response_model=LanguageSchema)
def get_language_by_abbreviation(abbreviation: str):
    return LanguageController.get_language_by_abbreviation(abbreviation)


@language_router.get("/get-all-languages", response_model=list[LanguageSchema])
def get_all_languages():
    return LanguageController.get_all_languages()


@language_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_language_by_id(language_id: str):
    return LanguageController.delete_language_by_id(language_id)
