from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.actors_actresses.exceptions import ActorActressNotFoundException

from app.actors_actresses.models import ActorActress


class ActorActressRepository:
    def __init__(self, db: Session):
        self.db = db

    ##superuser
    def create_actor_actress(self, name, surname, gender, about):
        try:
            actor_actress = ActorActress(name, surname, gender, about)
            self.db.add(actor_actress)
            self.db.commit()
            self.db.refresh(actor_actress)
            return actor_actress
        except IntegrityError as e:
            raise e

    def get_actor_actress_by_id(self, actor_actress_id: str):
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

    # lista
    def get_actor_actress_by_name(self, name: str):
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

    # lista
    def get_actor_actress_by_surname(self, surname: str):
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

    def get_all_actors_actresses(self):
        actors_actresses = self.db.query(ActorActress).all()
        if (actors_actresses is None) or (actors_actresses == []):
            raise ActorActressNotFoundException(
                message=f"The list is empty!",
                code=400,
            )
        return actors_actresses

    ##superuser
    def delete_actor_actress_by_id(self, actor_actress_id: str):
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
            raise e

    def order_actor_actress_by_name_decs(self):
        order_by_name_desc = (
            self.db.query(ActorActress).order_by(ActorActress.name.desc()).all()
        )
        return order_by_name_desc

    def order_actor_actress_by_name_asc(self):
        order_by_name_asc = (
            self.db.query(ActorActress).order_by(ActorActress.name.asc()).all()
        )
        return order_by_name_asc
