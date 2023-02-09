from fastapi import HTTPException, Response
from app.awards.services import AwardServices


class AwardController:
    @staticmethod
    def create_award(category, subcategory):
        try:
            award = AwardServices.create_award(category, subcategory)
            return award
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_id(award_id: str):
        award = AwardServices.get_award_by_id(award_id)
        if award:
            return award
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Award with provided id {award_id} does not exist",
            )

    @staticmethod
    def get_award_by_category(category: str):
        award = AwardServices.get_award_by_category(category)
        if award:
            return award
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Award with provided category {category} does not exist",
            )

    @staticmethod
    def get_award_by_subcategory(subcategory: str):
        award = AwardServices.get_award_by_subcategory(subcategory)
        if award:
            return award
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Award with provided subcategory {subcategory} does not exist",
            )

    @staticmethod
    def get_all_awards():
        awards = AwardServices.get_all_awards()
        return awards

    @staticmethod
    def delete_award_by_id(award_id: str):
        try:
            AwardServices.delete_award_by_id(award_id)
            return Response(content=f"Award with provided id - {award_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
