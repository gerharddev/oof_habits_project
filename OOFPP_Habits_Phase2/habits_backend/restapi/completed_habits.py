"""Completed Habits endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *
from habits_backend.services.completed_habits import completed_habits_service

router = APIRouter()


@router.get("/completed_habits/", response_model=list[schemas.Habit], tags=["completed_habits"])
async def get_all(skip: int = 0, limit: int = 100):
    with get_db() as session:
        completed_habits = completed_habits_service.get_all(skip=skip, limit=limit)

    return completed_habits


@router.get("/completed_habit/", response_model=schemas.CompletedHabit, tags=["completed_habits"])
async def get_by_id(completed_habit_id):
    with get_db() as session:
        completed_habit = completed_habits_service.get_by_id(completed_habit_id)

    return completed_habit


@router.post("/completed_habits/", response_model=schemas.CompletedHabit, tags=["completed_habits"])
async def create_habit(completed_habit: schemas.CompletedHabitCreate):
    return completed_habits_service.create(completed_habit=completed_habit)

