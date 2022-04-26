"""
Defines Habits service.

Information:
    pydantic - pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
    https://pydantic-docs.helpmanual.io/
"""
from typing import List
import habits_backend.schemas.frequencies as schema
from habits_backend.database.connectors import *
import habits_backend.crud.frequencies as crud


class FrequenciesService:
    """The Frequency service."""

    @classmethod
    def get_all(cls) -> List[schema.Frequency]:
        """Returns a list casters ordered by ID"""
        with get_db() as session:
            db_frequencies = crud.get_frequencies(session)
        frequencies = [schema.Frequency.from_orm(h) for h in db_frequencies]
        # from_orm: loads data into a model from an arbitrary class
        return frequencies


frequencies_service = FrequenciesService()
