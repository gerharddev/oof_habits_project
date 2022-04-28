"""Frequencies endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.frequencies as schemas
from habits_backend.services.frequencies import frequencies_service

router = APIRouter()


@router.get("/frequencies/", response_model=list[schemas.Frequency], tags=["frequencies"])
async def get_all_frequencies():
    return frequencies_service.get_all()


@router.post("/frequencies/", response_model=schemas.Frequency, tags=["frequencies"])
async def create_frequency(frequency: schemas.FrequencyCreate):
    return frequencies_service.create(frequency=frequency)

