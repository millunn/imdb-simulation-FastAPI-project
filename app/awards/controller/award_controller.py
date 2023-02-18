from fastapi import HTTPException, Response
from app.awards.exceptions import AwardNotFoundException
from app.awards.services import AwardServices
from sqlalchemy.exc import IntegrityError


class AwardController:
    @staticmethod
    def create_award(category, subcategory):
        try:
            award = AwardServices.create_award(category, subcategory)
            return award
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Award with provided category - {category} and subcategory - {subcategory} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_id(award_id: str):
        try:
            award = AwardServices.get_award_by_id(award_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_category(category: str):
        try:
            award = AwardServices.get_award_by_category(category)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_award_by_subcategory(subcategory: str):
        try:
            award = AwardServices.get_award_by_subcategory(subcategory)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_awards():
        try:
            awards = AwardServices.get_all_awards()
            return awards
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_award_by_id(award_id: str):
        try:
            if AwardServices.delete_study_programme_by_id(award_id):
                return Response(
                    content=f"Award with provided ID: {award_id} deleted.",
                    status_code=200,
                )
        except AwardNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def order_awards_by_category_decs():
        try:
            order_by_title_desc = AwardServices.order_awards_by_category_decs()
            return order_by_title_desc
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def order_awards_by_category_asc():
        try:
            order_by_category_asc = AwardServices.order_awards_by_category_asc()
            return order_by_category_asc
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
