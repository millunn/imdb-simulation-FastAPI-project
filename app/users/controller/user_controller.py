from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.users.exceptions import UserInvalidPasswordException, UserNotFoundException
from app.users.services import (
    UserServices,
    send_confirmation_email,
    send_email_login_alert,
    signJWT,
)


class UserController:
    @staticmethod
    def create_user(name, surname, email, password):
        try:
            user = UserServices.create_user(name, surname, email, password)
            send_confirmation_email(email)
            return user
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(name, surname, email, password):
        try:
            user = UserServices.create_super_user(name, surname, email, password)
            send_confirmation_email(email)
            return user
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password):
        try:
            user = UserServices.login_user(email, password)
            send_email_login_alert(email)
            if user.is_superuser:
                return signJWT(user.id, "super_user")
            return signJWT(user.id, "classic_user")
        except UserInvalidPasswordException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_id(user_id: str):
        try:
            user = UserServices.get_user_by_id(user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_users():
        try:
            users = UserServices.get_all_users()
            return users
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            print(e)

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserServices.delete_user_by_id(user_id)
            return Response(content=f"User with id - {user_id} is deleted")
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_user_name(user_id: str, name: str):
        try:
            user = UserServices.update_user_name(user_id, name)
            return user
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_surname(user_id: str, surname: str):
        try:
            user = UserServices.update_user_surname(user_id, surname)
            return user
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            user = UserServices.update_user_is_active(user_id, is_active)
            return user
        except UserNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
