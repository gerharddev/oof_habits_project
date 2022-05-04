"""Completed Habits endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *
from habits_backend.services.completed_habits import completed_habits_service

router = APIRouter(
    prefix="/completed-habits",
    tags=["completed-habits"],
    responses={404: {"description": "Not found"}})


@router.get("", response_model=list[schemas.CompletedHabitCreate])
async def get_all(skip: int = 0, limit: int = 100):
    with get_db() as session:
        completed_habits = completed_habits_service.get_all(skip=skip, limit=limit)

    return completed_habits


@router.get("/{habit-id}", response_model=list[schemas.CompletedHabitCreate],
            tags=["completed_habits"])
async def get_by_habit_id(habit_id, skip: int = 0, limit: int = 100):
    with get_db() as session:
        completed_habit = completed_habits_service.get_by_id(habit_id, skip=skip, limit=limit)

    return completed_habit


@router.get("/{habit-id}/detailed", response_model=list[schemas.CompletedHabit])
async def get_by_habit_id_detailed(habit_id, skip: int = 0, limit: int = 100):
    with get_db() as session:
        completed_habit = completed_habits_service.get_by_id_detailed(habit_id, skip=skip, limit=limit)

    return completed_habit


@router.post("", response_model=schemas.CompletedHabit)
async def create_habit(completed_habit: schemas.CompletedHabitCreate):
    return completed_habits_service.create(completed_habit=completed_habit)

