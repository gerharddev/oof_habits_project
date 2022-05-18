"""
Defines Completed Habits service.
"""
from typing import List
from fastapi.responses import JSONResponse
import habits_backend.schemas.habits_metadata as schemas
from habits_backend.database.connectors import *
import habits_backend.crud.analysis as crud
import habits_backend.modules.analysis as analyse
from habits_backend.services.completed_habits import completed_habits_service as completed_service
from habits_backend.services.habits import habits_service

class AnalysisService:
    """The Analysis service.
    It will call analysis module written using the functional programming paradigm"""
    @classmethod
    def get_all_details(cls) -> List[dict]:
        """Returns a list of habits being tracked.
        This mean a habit that was completed at least once"""
        with get_db() as session:
            db_details = crud.get_habit_with_details(session)

        # details = [schemas.HabitMetadata.from_orm(h) for h in db_details]
        return db_details

    @classmethod
    def get_tracked_habits(cls) -> List[dict]:
        """Returns a list of habits being tracked.
        This mean a habit that was completed at least once"""
        with get_db() as session:
            db_details = crud.get_habit_with_details(session)

        if db_details is not None:
            tracked = analyse.get_tracked_habits(db_details)
            # TODO: details = [schemas.HabitMetadata.from_orm(h) for h in db_details]
            return tracked

        return JSONResponse(status_code=404, content={"message": "No habit is tracked!"})

    @classmethod
    def get_equal_periodicity(cls, frequency='daily') -> List[dict]:
        """Returns a list of habits with the same periodicity."""

        with get_db() as session:
            db_details = crud.get_habit_with_details(session)

        if db_details is not None:
            tracked = analyse.get_equal_periodicity(db_details, frequency)
            # details = [schemas.HabitMetadata.from_orm(h) for h in db_details]
            if len(tracked) > 0:
                return tracked

        return JSONResponse(status_code=404, content={"message": "No habit with the same periodicity found!"})

    @classmethod
    def get_streak_by_habit_id(cls, habit_id) -> dict:
        """Returns the longest steak for a habit by habit id."""
        db_completed = completed_service.get_by_id(habit_id)
        frequency = habits_service.get_frequency(habit_id)

        if db_completed is None or frequency is None:
            return JSONResponse(status_code=404, content={"message": "No habit with this id found"})

        return analyse.get_streak_by_habit_id(db_completed, frequency)

    @classmethod
    def get_longest_streak(cls, habit_id) -> List[dict]:
        # TODO
        # Get a list of all completed habits
        # Get the longest streak per habit id
        # Return the longest streak for a habit
        return []

analysis_service = AnalysisService()


# 1. All currently tracked habits : Habits that have data in the completed habits table
# 2. All habits with the same period - day, month
# 3. Which habit has the longest run streak
# 4. Longest run streak for a habit
