"""
Defines Seed service used to load sample data to the database.
"""
import json
from fastapi import HTTPException
from habits_backend.database.connectors import *
import habits_backend.crud.frequencies as crud


class SeedingService:
    """The Habit service."""

    @classmethod
    def frequencies(cls):
        """Returns a habit by ID."""
        with get_db() as session:
            if not crud.has_frequencies(session):
                with open("./database/data/frequencies.json") as f:
                    data = json.load(f)
                    if len(data) > 0:
                        return crud.recreate_frequencies(db=session, frequencies=data)

    @classmethod
    def sample_data(cls):
        print("Seed sample data")
        # TODO: Clear and load data


seeding_service = SeedingService()

