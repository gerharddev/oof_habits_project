"""Analysis endpoints"""

from fastapi import APIRouter
from habits_backend.database.connectors import *
from habits_backend.services.analysis import analysis_service
import habits_backend.schemas.habits_metadata as schemas

router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    responses={404: {"description": "Not found"}})


@router.get("/tracked", response_model=list[dict])
async def get_tracked_habits():
    with get_db() as session:
        tracked = analysis_service.get_tracked_habits()

    return tracked


@router.get("/metadata", response_model=list[dict])
async def get_tracked_habits():
    with get_db() as session:
        tracked = analysis_service.get_all_details()

    return tracked


@router.get("/equal_periodicity/{frequency}",  response_model=list[dict])
async def get_equal_periodicity(frequency):
    with get_db() as session:
        tracked = analysis_service.get_equal_periodicity(frequency)

    return tracked
