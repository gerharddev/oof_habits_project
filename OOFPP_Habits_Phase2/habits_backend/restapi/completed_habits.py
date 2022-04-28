"""Completed Habits endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *
from habits_backend.services.completed_habits import completed_habits_service

router = APIRouter()


@router.get("/completed-habits/", response_model=list[schemas.CompletedHabit], tags=["completed_habits"])
async def get_all(skip: int = 0, limit: int = 100):
    with get_db() as session:
        completed_habits = completed_habits_service.get_all(skip=skip, limit=limit)

    return completed_habits


@router.get("/completed-habits-by-id/{habit-id}", response_model=list[schemas.CompletedHabit], tags=["completed_habits"])
async def get_by_habit_id(habit_id, skip: int = 0, limit: int = 100):
    with get_db() as session:
        completed_habit = completed_habits_service.get_by_id(habit_id, skip=skip, limit=limit)

    return completed_habit


@router.post("/completed-habits/", response_model=schemas.CompletedHabit, tags=["completed_habits"])
async def create_habit(completed_habit: schemas.CompletedHabitCreate):
    return completed_habits_service.create(completed_habit=completed_habit)

