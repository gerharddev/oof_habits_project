"""
Defines Habits service.
"""
from typing import List
from fastapi import HTTPException
import habits_backend.schemas.habits as schemas
from habits_backend.database.connectors import *
import habits_backend.crud.habits as crud


# Habits service class
class HabitsService:
    """The Habit service class."""

    # Declare a class method. Can be called by using habits_service.get_by_id() (classname.methodname())
    @classmethod
    def get_by_id(cls, habit_id) -> schemas.Habit:
        """Returns a habit by ID."""
        with get_db() as session:
            db_habit = crud.get_habit_by_id(session, habit_id)

        return schemas.Habit.from_orm(db_habit) if db_habit is not None else None

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def get_all(cls, skip, limit) -> List[schemas.Habit]:
        """Returns a list of habits ordered by ID."""
        with get_db() as session:
            db_habits = crud.get_habits(session, skip, limit)

        habits = [schemas.Habit.from_orm(h) for h in db_habits]
        return habits

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def get_frequency(cls, habit_id) -> str:
        """Returns a frequency of a habit by habit ID."""
        with get_db() as session:
            return crud.get_frequency(session, habit_id) or None

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def create(cls, habit: schemas.HabitCreate):
        """Create a new habit."""
        with get_db() as session:
            db_habit = crud.get_habit_by_name(session, name=habit.name)
            if db_habit:
                raise HTTPException(status_code=400, detail="Habit with this name already exist")
        return crud.create_habit(db=session, habit=habit)

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def update(cls, habit: schemas.HabitUpdate):
        """Update a habit."""
        with get_db() as session:
            return crud.update_habit(db=session, habit=habit)

    # Declare a class method. Can be called by using classname.methodname()
    @classmethod
    def delete(cls, id: int):
        """Delete item by id."""
        with get_db() as session:
            return crud.delete(db=session, id=id)


# Create an instance of the HabitsService
habits_service = HabitsService()
