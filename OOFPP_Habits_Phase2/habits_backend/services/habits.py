"""
Defines Habits service.
"""
from typing import List
import habits_backend.schemas.habits as schema
from habits_backend.database.connectors import *
import habits_backend.crud.habits as crud


class HabitsService:
    """The Habit service."""

    @classmethod
    def get_all(cls) -> List[schema.Habit]:
        """Returns a list casters ordered by ID"""
        with get_db() as session:
            db_habits = crud.get_habits(session)
        habits = [schema.Habit(h) for h in db_habits]
        return habits


habits_service = HabitsService()
