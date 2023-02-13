from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.actors_actressees.exceptions import ActorActressNotFoundException
from app.actors_actressees.models import ActorActressAward
from app.actors_actressees.models import ActorActress
from app.awards.exceptions import AwardNotFoundException
from app.awards.models import Award


class ActorActressAwardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_actor_actress_award(self, actor_actress_id, award_id):
        try:
            actor_actress_award = ActorActressAward(actor_actress_id, award_id)
            self.db.add(actor_actress_award)
            self.db.commit()
            self.db.refresh(actor_actress_award)
            return actor_actress_award
        except IntegrityError as e:
            raise e

    def get_award_by_actor_actress_id(self, actor_actress_id: str):
        award_by_actor_actress_id = (
            self.db.query(ActorActressAward)
            .filter(ActorActressAward.actor_actress_id == actor_actress_id)
            .all()
        )
        print(award_by_actor_actress_id)
        if award_by_actor_actress_id is None:
            raise AwardNotFoundException(
                message=f"Award with provided actor/actress id: {actor_actress_id} not found",
                code=400,
            )
        return award_by_actor_actress_id

    def get_actor_actress_by_award_id(self, award_id: str):
        actor_actress_by_award_id = (
            self.db.query(ActorActressAward)
            .filter(ActorActressAward.award_id == award_id)
            .all()
        )
        if actor_actress_by_award_id is None:
            raise ActorActressNotFoundException(
                message=f"Actor/actress with provided award id: {award_id} not found",
                code=400,
            )
        return actor_actress_by_award_id

    def get_all_actor_actresss_with_all_awards(self):
        actor_actresss_award = self.db.query(ActorActressAward).all()
        return actor_actresss_award

    # # lista
    # def get_actor_actress_by_name(self, name: str):
    #     actor_actress = (
    #         self.db.query(ActorActressAward)
    #         .filter(ActorActressAward.name == name)
    #         .all()
    #     )
    #     return actor_actress

    # # lista
    # def get_actor_actress_by_surname(self, surname: str):
    #     actor_actress = (
    #         self.db.query(ActorActressAward)
    #         .filter(ActorActressAward.surname == surname)
    #         .all()
    #     )
    #     return actor_actress
