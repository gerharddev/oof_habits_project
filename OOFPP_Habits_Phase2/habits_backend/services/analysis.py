"""
Defines Completed Habits service.
"""
from typing import List
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *
import habits_backend.crud.analysis as crud


class AnalysisService:
    """The Analysis service.
    It will call analysis module written using the functional programming paradigm"""


    @classmethod
    def get_all_details(cls) -> List[str]:
        """Returns a list of habits being tracked.
        This mean a habit that was completed at least once"""
        with get_db() as session:
            db_details = crud.get_habit_with_details(session)

        # habits = [] #[schemas.CompletedHabitCreate.from_orm(h) for h in db_habits]
        return db_details


analysis_service = AnalysisService()
