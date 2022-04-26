"""Frequencies endpoints"""

from fastapi import APIRouter, HTTPException
from habits_backend.crud.frequencies import *
# from habits_backend.database.connectors import *
from habits_backend.schemas.frequencies import *
from habits_backend.database.connectors import SessionLocal, engine

router = APIRouter()
# Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/frequencies/", response_model=list[Frequency], tags=["frequencies"])
async def read_frequencies(skip: int = 0, limit: int = 100):
    with get_db() as session:
        frequencies = get_frequencies(session, skip=skip, limit=limit)

    return frequencies


@router.post("/frequencies/", response_model=Frequency)
async def create_frequency(frequency: FrequencyCreate):
    with get_db() as session:
        db_frequency = get_frequency_by_name(session, name=frequency.name)
        if db_frequency:
            raise HTTPException(status_code=400, detail="Frequency already exist")
    return create_frequency(db=session, frequency=frequency)
