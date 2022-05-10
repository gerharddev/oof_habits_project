"""
Defines Seed service used to load sample data to the database.
"""
import json
from fastapi import HTTPException
from habits_backend.database.connectors import *
import habits_backend.crud.frequencies as frequencies_crud
import habits_backend.crud.habits as habits_crud


def get_data(filename):
    with open(filename) as f:
        return json.load(f)


class SeedingService:
    """The Habit service."""

    @classmethod
    def frequencies(cls):
        """Load frequencies if they do not exist."""
        with get_db() as session:
            if not frequencies_crud.has_frequencies(session):
                data = get_data("./database/data/frequencies.json")
                if len(data) > 0:
                    return frequencies_crud.recreate_frequencies(db=session, frequencies=data)

    @classmethod
    def sample_data(cls):
        """Load sample data to demonstrate application functionality."""

        with get_db() as db:
            cls.load_habits(db)

    @classmethod
    def load_habits(cls, db):
        # Habits
        data = get_data("./database/data/habits.json")
        dedupe = []
        for item in data:
            # Remove duplicate values
            if habits_crud.get_habit_by_name(db, item["name"]) is None:
                dedupe.append(item)
        habits_crud.create_habits(db, dedupe)

    @classmethod
    def load_completed_habits(cls, db):
        # Completed Habits
        data = get_data("./database/data/completed_habits.json")
        dedupe = []
        for item in data:
            # Remove duplicate values
            if habits_crud.get_habit_by_name(db, item["name"]) is None:
                dedupe.append(item)
        habits_crud.create_habits(db, dedupe)


seeding_service = SeedingService()

