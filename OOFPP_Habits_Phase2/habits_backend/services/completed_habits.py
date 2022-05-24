"""
Defines Completed Habits service.
"""
from typing import List
from fastapi.responses import JSONResponse
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *
import habits_backend.crud.completed_habits as crud


class CompletedHabitsService:
    """The Completed Habit service."""

    @classmethod
    def get_by_id(cls, habit_id, skip: int = 0, limit: int = 100) -> List[schemas.CompletedHabitQuery]:
        """Returns a completed habit by ID."""
        with get_db() as session:
            db_habits = crud.get_by_id(session, habit_id)

        if len(db_habits) <= 0:
            return JSONResponse(status_code=404, content={"message": "No completed habits found"})

        habits = [schemas.CompletedHabitQuery.from_orm(h) for h in db_habits]
        return habits

    @classmethod
    def get_by_id_detailed(cls, habit_id, skip, limit) -> List[schemas.CompletedHabit]:
        """Returns a completed habit by ID."""
        with get_db() as session:
            db_habits = crud.get_by_id_detailed(session, habit_id)

        habits = [schemas.CompletedHabit.from_orm(h) for h in db_habits]
        return habits

    @classmethod
    def get_all(cls, skip, limit) -> List[schemas.CompletedHabitQuery]:
        """Returns a list of completed habits ordered by completed date."""
        with get_db() as session:
            db_habits = crud.get_all(session, skip, limit)

        habits = [schemas.CompletedHabitQuery.from_orm(h) for h in db_habits]
        return habits

    @classmethod
    def create(cls, completed_habit: schemas.CompletedHabitCreate):
        """Create a new completed habit."""
        with get_db() as session:
            return crud.create(db=session, completed_habit=completed_habit)


completed_habits_service = CompletedHabitsService()
