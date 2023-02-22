from fastapi import APIRouter, Depends

from app.users.controller import UserController
from app.users.controller.user_auth_controller import JWTBearer
from app.users.schemas import *

user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post(
    "/add-new-user",
    response_model=UserSchema,
    dependencies=[Depends(JWTBearer("classic_user"))],
)
def create_user(user: UserSchemaIn):
    return UserController.create_user(
        user.name, user.surname, user.email, user.password
    )


@user_router.post(
    "/add-new-super-user",
    response_model=UserSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(
        user.name, user.surname, user.email, user.password
    )


@user_router.post("/login")
def login_user(user: UserSchemaLogIn):
    return UserController.login_user(user.email, user.password)


@user_router.get(
    "/id",
    response_model=UserSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get(
    "/get-all-users",
    response_model=list[UserSchema],
    dependencies=[Depends(JWTBearer("super_user"))],
)
def get_all_users():
    return UserController.get_all_users()


@user_router.delete(
    "/",
    dependencies=[Depends(JWTBearer("super_user"))],
)
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@user_router.put("/name-update/name", response_model=UserSchema)
def update_user_name(user_id: str, update_data: UserSchemaUpdateName):
    return UserController.update_user_name(user_id, update_data.name)


@user_router.put("/surname-update/surname", response_model=UserSchema)
def update_user_surname(user_id: str, update_data: UserSchemaUpdateSurname):
    return UserController.update_user_surname(user_id, update_data.surname)


@user_router.put("/is-active-update/is_active", response_model=UserSchema)
def update_user_is_active(user_id: str, update_data: UserSchemaUpdateActivity):
    return UserController.update_user_is_active(user_id, update_data.is_active)
