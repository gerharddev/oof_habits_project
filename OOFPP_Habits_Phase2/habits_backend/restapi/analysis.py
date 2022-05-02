"""Analysis endpoints"""

from fastapi import APIRouter
from habits_backend.database.connectors import *
from habits_backend.services.analysis import analysis_service

router = APIRouter()


@router.get("/tracked_habits/", response_model=list[str], tags=["analysis"])
async def get_tracked_habits():
    with get_db() as session:
        tracked = analysis_service.get_all_details()

    return tracked


