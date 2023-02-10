from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.actors_actressees.models import ActorActress


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
        return actor_actress

    # lista
    def get_actor_actress_by_name(self, name: str):
        actor_actress = (
            self.db.query(ActorActress).filter(ActorActress.name == name).all()
        )
        return actor_actress

    # lista
    def get_actor_actress_by_surname(self, surname: str):
        actor_actress = (
            self.db.query(ActorActress).filter(ActorActress.surname == surname).all()
        )
        return actor_actress

    def get_all_actor_actresss(self):
        actor_actresss = self.db.query(ActorActress).all()
        return actor_actresss

    ##superuser
    def delete_actor_actress_by_id(self, actor_actress_id: str):
        try:
            actor_actress = (
                self.db.query(ActorActress)
                .filter(ActorActress.id == actor_actress_id)
                .first()
            )
            self.db.delete(actor_actress)
            self.db.commit()
            return True
        except Exception as e:
            raise e
