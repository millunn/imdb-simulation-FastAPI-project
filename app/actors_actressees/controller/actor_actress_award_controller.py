from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.actors_actressees.exceptions import ActorActressNotFoundException
from app.actors_actressees.services import ActorActressAwardServices
from app.awards.exceptions import AwardNotFoundException


class ActorActressAwardController:
    @staticmethod
    def create_actor_actress_award(actor_actress_id, award_id):
        try:
            actor_actress_award = ActorActressAwardServices.create_actor_actress_award(
                actor_actress_id, award_id
            )
            return actor_actress_award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Already in database")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_actor_actress_id(actor_actress_id: str):
        try:
            award = ActorActressAwardServices.get_award_by_actor_actress_id(
                actor_actress_id
            )
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_actor_actress_by_award_id(award_id: str):
        try:
            actor_actress = ActorActressAwardServices.get_actor_actress_by_award_id(
                award_id
            )
            return actor_actress
        except ActorActressNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_actor_actresss_with_all_awards():
        try:
            actor_actress_award = (
                ActorActressAwardServices.get_all_actor_actresss_with_all_awards()
            )
            return actor_actress_award
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
