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
        print("Seed frequencies")
        # Check data and load
        with open("./database/data/frequencies.json") as f:
            data = json.load(f)
            if len(data) > 0:
                with get_db() as session:
                    # db_frequency = crud.get_frequency_by_name(session, name=frequency.name)
                    # if db_frequency:
                    #     raise HTTPException(status_code=400, detail="Frequency already exist")
                    return crud.create_frequencies(db=session, frequencies=data)
            # TODO: Import data
            print("Import")
        return

    @classmethod
    def sample_data(cls):
        print("Seed sample data")
        # TODO: Clear and load data


seeding_service = SeedingService()

