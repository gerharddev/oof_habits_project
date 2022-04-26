"""Frequencies endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.frequencies as schema
from habits_backend.database.connectors import *
import habits_backend.crud.frequencies as crud

router = APIRouter()


@router.get("/frequencies/", response_model=list[schema.Frequency], tags=["frequencies"])
async def read_frequencies(skip: int = 0, limit: int = 100):
    with get_db() as session:
        frequencies = crud.get_frequencies(session, skip=skip, limit=limit)

    return frequencies

#
# @router.post("/frequencies/", response_model=Frequency)
# async def create_frequency(frequency: FrequencyCreate):
#     with get_db() as session:
#         db_frequency = get_frequency_by_name(session, name=frequency.name)
#         if db_frequency:
#             raise HTTPException(status_code=400, detail="Frequency already exist")
#     return create_frequency(db=session, frequency=frequency)
