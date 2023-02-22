""" User Services module """

import hashlib

from app.db.database import SessionLocal
from app.users.exceptions.exceptions import UserInvalidPasswordException
from app.users.repository import UserRepository


class UserServices:
    """User model services"""

    @staticmethod
    def create_user(name, surname, email, password: str):
        """Create new user"""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(
                    name, surname, email, hashed_password
                )
            except Exception as e:
                raise e from e

    def create_super_user(name, surname, email, password: str):
        """Create new superuser"""
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(
                    name, surname, email, hashed_password
                )
            except Exception as e:
                raise e from e

    @staticmethod
    def get_user_by_id(user_id: str):
        """Get user by id"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_id(user_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def get_all_users():
        """Get all users"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_all_users()
        except Exception as e:
            raise e from e

    @staticmethod
    def delete_user_by_id(user_id: str):
        """Delete user by id"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e from e

    @staticmethod
    def update_user_name(user_id: str, name: str):
        """Update user name section"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_name(user_id, name)
        except Exception as e:
            raise e from e

    @staticmethod
    def update_user_surname(user_id: str, surname: str):
        """Update user surname section"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_surname(user_id, surname)
        except Exception as e:
            raise e from e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """Update user is_active section"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
        except Exception as e:
            raise e from e

    @staticmethod
    def login_user(email: str, password: str):
        """User log in"""
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email)
                if (
                    hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                    != user.password
                ):
                    raise UserInvalidPasswordException(
                        message="Invalid password for user", code=401
                    )
                return user
        except Exception as e:
            raise e from e
