from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.exceptions import UserNotFoundException
from app.users.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name, surname, email, password):
        try:
            user = User(name, surname, email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, name, surname, email, password):
        try:
            user = User(
                name=name,
                surname=surname,
                email=email,
                password=password,
                is_superuser=True,
            )
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_user_by_id(self, user_id: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise UserNotFoundException(
                f"User with provided id: {user_id} not found.", 400
            )
        return user

    def get_user_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            raise UserNotFoundException(
                f"User with provided email: {email} not found.", 400
            )
        return user

    def get_all_users(self):
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id: str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise UserNotFoundException(
                    f"User with provided id: {user_id} not found.", 400
                )
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_user_name(self, user_id: str, name: str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise UserNotFoundException(
                    f"User with provided id: {user_id} not found.", 400
                )
            user.name = name
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_user_surname(self, user_id: str, surname: str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise UserNotFoundException(
                    f"User with provided id: {user_id} not found.", 400
                )
            user.surname = surname
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_user_is_active(self, user_id: str, is_active: bool):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise UserNotFoundException(
                    f"User with provided id: {user_id} not found.", 400
                )
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e
