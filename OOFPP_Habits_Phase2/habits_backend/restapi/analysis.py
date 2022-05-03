"""Analysis endpoints"""

from fastapi import APIRouter
from habits_backend.database.connectors import *
from habits_backend.services.analysis import analysis_service
import habits_backend.schemas.habits_metadata as schemas

router = APIRouter()


@router.get("/tracked_habits/", response_model=list[dict], tags=["analysis"])
async def get_tracked_habits():
    with get_db() as session:
        tracked = analysis_service.get_tracked_habits()    # TODO: only return tracked

    return tracked


@router.get("/habits_metadata/", response_model=list[dict], tags=["analysis"])
async def get_tracked_habits():
    with get_db() as session:
        tracked = analysis_service.get_all_details()

    return tracked

