"""
Defines Completed Habits service.
"""
from typing import List
import habits_backend.schemas.habits_metadata as schemas
from habits_backend.database.connectors import *
import habits_backend.crud.analysis as crud


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
            db_details = crud.get_tracked_habits(session)   # TODO: Call functional model

        # details = [schemas.HabitMetadata.from_orm(h) for h in db_details]
        return db_details


analysis_service = AnalysisService()


# 1. All currently tracked habits : Habits that have data in the completed habits table
# 2. All habits with the same period - day, month
# 3. Which habit has the longest run streak
# 4. Longest run streak for a habit

# - return a list of all currently tracked habits,
# - return a list of all habits with the same periodicity,
# - return the longest run streak of all defined habits,
# - and return the longest run streak for a given habit.