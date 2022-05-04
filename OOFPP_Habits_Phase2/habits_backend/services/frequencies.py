"""
Defines Habits service.

Information:
    pydantic - pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
    https://pydantic-docs.helpmanual.io/
"""
from typing import List
from fastapi import HTTPException

import habits_backend.schemas.frequencies as schemas
from habits_backend.database.connectors import *
import habits_backend.crud.frequencies as crud


class FrequenciesService:
    """The Frequency service."""

    @classmethod
    def get_all(cls) -> List[schemas.Frequency]: # TODO: skip and limit
        """Returns a list of frequencies order by ID."""
        with get_db() as session:
            db_frequencies = crud.get_frequencies(session)
        frequencies = [schemas.Frequency.from_orm(h) for h in db_frequencies]

        return frequencies

    @classmethod
    def create(cls, frequency: schemas.FrequencyCreate):
        """Create a new frequency."""
        with get_db() as session:
            db_frequency = crud.get_frequency_by_name(session, name=frequency.name)
            if db_frequency:
                raise HTTPException(status_code=400, detail="Frequency already exist")
        return crud.create_frequency(db=session, frequency=frequency)


frequencies_service = FrequenciesService()
