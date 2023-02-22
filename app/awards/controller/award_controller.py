""" Award Controller module """

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.awards.exceptions import AwardNotFoundException
from app.awards.services import AwardServices


class AwardController:
    """Award model controller"""

    @staticmethod
    def create_award(category, subcategory):
        """Create new award"""
        try:
            award = AwardServices.create_award(category, subcategory)
            return award
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Award with provided category - {category} and subcategory - {subcategory} already exists.",
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_id(award_id: str):
        """Get award by id"""
        try:
            award = AwardServices.get_award_by_id(award_id)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_category(category: str):
        """Get award by category"""
        try:
            award = AwardServices.get_award_by_category(category)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_award_by_subcategory(subcategory: str):
        """Get award by subcategory"""
        try:
            award = AwardServices.get_award_by_subcategory(subcategory)
            return award
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_awards():
        """Get all awards"""
        try:
            awards = AwardServices.get_all_awards()
            return awards
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_award_by_id(award_id: str):
        """Delete award by id"""
        try:
            if AwardServices.delete_award_by_id(award_id):
                return Response(
                    content=f"Award with provided ID: {award_id} deleted.",
                    status_code=200,
                )
        except AwardNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def order_awards_by_category_decs():
        """Order awards by category in decsending order"""
        try:
            order_by_title_desc = AwardServices.order_awards_by_category_decs()
            return order_by_title_desc
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def order_awards_by_category_asc():
        """Order awards by category in acsending order"""
        try:
            order_by_category_asc = AwardServices.order_awards_by_category_asc()
            return order_by_category_asc
        except AwardNotFoundException as e:
            raise HTTPException(
                status_code=e.code,
                detail=e.message,
            ) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
