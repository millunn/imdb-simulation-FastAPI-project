from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.actors_actressees.services import ActorActressAwardServices


class ActorActressAwardController:
    @staticmethod
    def create_actor_actress_award(actor_actress_id, award_id):
        try:
            actor_actress_award = ActorActressAwardServices.create_actor_actress_award(
                actor_actress_id, award_id
            )
            return actor_actress_award
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        award = ActorActressAwardServices.get_award_by_actor_actress_id(
            actor_actress_id
        )
        if award:
            return award
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Actor/actress with provided id {actor_actress_id} does not exist",
            )

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        actor_actress = ActorActressAwardServices.get_actor_actress_by_award_id(
            award_id
        )
        if actor_actress:
            return actor_actress
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Award with provided id {award_id} does not exist",
            )

    @staticmethod
    def get_all_actor_actresss_with_all_awards():
        actor_actress_award = (
            ActorActressAwardServices.get_all_actor_actresss_with_all_awards()
        )
        return actor_actress_award
