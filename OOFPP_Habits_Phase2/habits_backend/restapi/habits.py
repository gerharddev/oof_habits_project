"""Habits endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.habits as schemas
from habits_backend.database.connectors import *
from habits_backend.services.habits import habits_service

router = APIRouter()


@router.get("/habits/", response_model=list[schemas.Habit], tags=["habits"])
async def get_all_habits(skip: int = 0, limit: int = 100):
    with get_db() as session:
        habits = habits_service.get_all(skip=skip, limit=limit)

    return habits


@router.get("/habit/", response_model=schemas.Habit, tags=["habits"])
async def get_by_id(habit_id):
    with get_db() as session:
        habit = habits_service.get_by_id(habit_id)

    return habit


@router.post("/habits/", response_model=schemas.Habit, tags=["habits"])
async def create_habit(habit: schemas.HabitCreate):
    return habits_service.create(habit=habit)

