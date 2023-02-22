""" Actor/Actress Repository module """

from sqlalchemy import desc, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.actors_actresses.exceptions import ActorActressNotFoundException
from app.actors_actresses.models import ActorActress


class ActorActressRepository:
    """Actor/Actress model repository"""

    def __init__(self, db: Session):
        self.db = db

    def create_actor_actress(self, name, surname, gender, about):
        """Create new actor_actress"""
        try:
            actor_actress = ActorActress(name, surname, gender, about)
            self.db.add(actor_actress)
            self.db.commit()
            self.db.refresh(actor_actress)
            return actor_actress
        except IntegrityError as e:
            raise e from e

    def get_actor_actress_by_id(self, actor_actress_id: str):
        """Get actor_actress by id"""
        actor_actress = (
            self.db.query(ActorActress)
            .filter(ActorActress.id == actor_actress_id)
            .first()
        )
        if actor_actress is None:
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided id: {actor_actress_id} not found.",
                code=400,
            )
        return actor_actress

    def get_actor_actress_by_name(self, name: str):
        """Get actor_actress by name"""
        actor_actress = (
            self.db.query(ActorActress)
            .filter(ActorActress.name.ilike(f"%{name}%"))
            .all()
        )
        if (actor_actress is None) or (actor_actress == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided name: {name} not found.", code=400
            )
        return actor_actress

    def get_actor_actress_by_surname(self, surname: str):
        """Get actor_actress by surname"""
        actor_actress = (
            self.db.query(ActorActress)
            .filter(ActorActress.surname.ilike(f"%{surname}%"))
            .all()
        )
        if (actor_actress is None) or (actor_actress == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided surname: {surname} not found.",
                code=400,
            )
        return actor_actress

    def get_actor_actress_by_gender(self, gender: str):
        """Get actor_actress by gender"""
        actor_actress = (
            self.db.query(ActorActress).filter(ActorActress.gender == gender).all()
        )
        if (actor_actress is None) or (actor_actress == []):
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided gender: {gender} not found.",
                code=400,
            )
        return actor_actress

    def get_all_actors_actresses(self):
        """Get all actors_actresses"""
        actors_actresses = self.db.query(ActorActress).all()
        if (actors_actresses is None) or (actors_actresses == []):
            raise ActorActressNotFoundException(
                message="The list is empty!",
                code=400,
            )
        return actors_actresses

    def delete_actor_actress_by_id(self, actor_actress_id: str):
        """Delete actor_actress by id"""
        try:
            actor_actress = (
                self.db.query(ActorActress)
                .filter(ActorActress.id == actor_actress_id)
                .first()
            )
            if actor_actress is None:
                raise ActorActressNotFoundException(
                    message=f"Actor/actress with provided id: {actor_actress_id} not found.",
                    code=400,
                )
            self.db.delete(actor_actress)
            self.db.commit()
            return True
        except Exception as e:
            raise e from e

    def order_actor_actress_by_name_decs(self):
        """Order actor_actress by name in decsending order"""
        order_by_name_desc = (
            self.db.query(ActorActress).order_by(ActorActress.name.desc()).all()
        )
        return order_by_name_desc

    def order_actor_actress_by_name_asc(self):
        """Order actor_actress by name in acsending order"""
        order_by_name_asc = (
            self.db.query(ActorActress).order_by(ActorActress.name.asc()).all()
        )
        return order_by_name_asc

    def get_gender_statistics(self):
        """Get gender statistics"""
        gender_statistics = (
            self.db.query(ActorActress)
            .group_by(ActorActress.gender)
            .order_by(desc("gender_count"))
            .values(
                ActorActress.gender.label("gender"),
                func.count(ActorActress.gender).label("gender_count"),
            )
        )
        return gender_statistics

    def update_actor_actress_about_section(self, actor_actress_id: str, about: str):
        """Update actor_actress about section"""
        try:
            actor_actress = (
                self.db.query(ActorActress)
                .filter(ActorActress.id == actor_actress_id)
                .first()
            )
            if actor_actress is None:
                raise ActorActressNotFoundException(
                    f"Actor/actress with provided id: {actor_actress_id} not found.",
                    400,
                )
            actor_actress.about = about
            self.db.add(actor_actress)
            self.db.commit()
            self.db.refresh(actor_actress)
            return actor_actress
        except Exception as e:
            raise e from e
