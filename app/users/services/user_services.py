import hashlib
from app.db.database import SessionLocal
from app.users.exceptions.exceptions import UserInvalidPassword
from app.users.repository.user_repository import UserRepository


class UserServices:
    @staticmethod
    def create_user(name, surname, email, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(
                    name, surname, email, hashed_password
                )
            except Exception as e:
                raise e

    def create_super_user(name, surname, email, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(
                    name, surname, email, hashed_password
                )
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_user_by_id(user_id)

    @staticmethod
    def get_all_users():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_name(user_id: str, name: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_name(user_id, name)
            except Exception as e:
                raise e

    @staticmethod
    def update_user_surname(user_id: str, surname: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_surname(user_id, surname)
            except Exception as e:
                raise e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email)
                if (
                    hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                    != user.password
                ):
                    raise UserInvalidPassword(
                        message="Invalid password for user", code=401
                    )
                return user
            except Exception as e:
                raise e
