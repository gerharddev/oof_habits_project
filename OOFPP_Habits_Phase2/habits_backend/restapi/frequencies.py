"""Frequencies endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.frequencies as schemas
from habits_backend.services.frequencies import frequencies_service

router = APIRouter(
    prefix="/frequencies",
    tags=["frequencies"],
    responses={404: {"description": "Not found"}})


@router.get("", response_model=list[schemas.Frequency])
async def get_all_frequencies():
    return frequencies_service.get_all()


# @router.post("", response_model=schemas.Frequency)
# async def create_frequency(frequency: schemas.FrequencyCreate):
#     return frequencies_service.create(frequency=frequency)

