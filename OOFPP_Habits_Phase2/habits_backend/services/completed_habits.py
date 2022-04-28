"""
Defines Completed Habits service.
"""
from typing import List
from fastapi import HTTPException
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *
import habits_backend.crud.completed_habits as crud


class CompletedHabitsService:
    """The Completed Habit service."""

    @classmethod
    def get_by_id(cls, habit_id) -> schemas.CompletedHabit:
        """Returns a completed habit by ID."""
        with get_db() as session:
            db_habit = crud.get_completed_habit_by_id(session, habit_id)

        return schemas.Habit.from_orm(db_habit)

    @classmethod
    def get_all(cls, skip, limit) -> List[schemas.Habit]:
        """Returns a list of completed habits ordered by completed date."""
        with get_db() as session:
            db_habits = crud.get_completed_habits(session, skip, limit)

        habits = [schemas.Habit.from_orm(h) for h in db_habits]
        return habits

    @classmethod
    def create(cls, completed_habit: schemas.CompletedHabitCreate):
        """Create a new completed habit."""
        with get_db() as session:
            return crud.create_completed_habit(db=session, completed_habit=completed_habit)


completed_habits_service = CompletedHabitsService()
