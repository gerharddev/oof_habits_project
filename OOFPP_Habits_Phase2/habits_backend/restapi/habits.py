"""Habits endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.habits as schema
from habits_backend.database.connectors import *
import habits_backend.crud.habits as crud

router = APIRouter()


@router.get("/habits/", response_model=list[schema.Habit], tags=["habits"])
async def read_habits(skip: int = 0, limit: int = 100):
    with get_db() as session:
        habits = crud.get_habits(session, skip=skip, limit=limit)

    return habits
