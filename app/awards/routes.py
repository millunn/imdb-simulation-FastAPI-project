from fastapi import APIRouter, Depends
from app.awards.controller import AwardController
from app.awards.schemas import AwardSchema, AwardSchemaIn
from app.users.controller.user_auth_controller import JWTBearer

award_router = APIRouter(tags=["awards"], prefix="/api/awards")


@award_router.post(
    "/add-new-award",
    response_model=AwardSchema,
    dependencies=[Depends(JWTBearer("super_user"))],
)
def create_award(award: AwardSchemaIn):
    return AwardController.create_award(award.category, award.subcategory)


@award_router.get("/id", response_model=AwardSchema)
def get_award_by_id(award_id: str):
    return AwardController.get_award_by_id(award_id)


@award_router.get("/category", response_model=AwardSchema)
def get_award_by_category(category: str):
    return AwardController.get_award_by_category(category)


@award_router.get("/subcategory", response_model=AwardSchema)
def get_award_by_subcategory(subcategory: str):
    return AwardController.get_award_by_subcategory(subcategory)


@award_router.get("/get-all-awards", response_model=list[AwardSchema])
def get_all_awards():
    return AwardController.get_all_awards()


@award_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_award_by_id(award_id: str):
    return AwardController.delete_award_by_id(award_id)
