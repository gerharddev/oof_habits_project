"""Habits endpoints."""

from fastapi import APIRouter
import habits_backend.schemas.habits as schemas
from habits_backend.database.connectors import *
from habits_backend.services.habits import habits_service
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/habits",
    tags=["habits"],
    responses={404: {"description": "Not found"}})


@router.get("", response_model=list[schemas.Habit])
async def get_all(skip: int = 0, limit: int = 100):
    with get_db() as session:
        habits = habits_service.get_all(skip=skip, limit=limit)

    return habits


@router.get("/{id}", response_model=schemas.Habit)
async def get_by_id(habit_id):
    with get_db() as session:
        habit = habits_service.get_by_id(habit_id)
    # TODO JsonResponse here
    return habit


@router.post("", response_model=schemas.Habit)
async def create_habit(habit: schemas.HabitCreate):
    return habits_service.create(habit=habit)


@router.put("", response_model=schemas.Habit)
async def update_habit(habit: schemas.HabitUpdate):
    # TODO: Only values that want to change, created date
    updated = habits_service.update(habit=habit)
    return JSONResponse(status_code=200, content={"message": "Updated"}) if updated is not None else JSONResponse(
        status_code=404, content={"message": "Habit not found"})


@router.delete("/{id}")
async def deleted_completed_habit(id: int):
    deleted = habits_service.delete(id=id)

    return JSONResponse(status_code=200, content={"message": "Deleted"}) if deleted is not None else JSONResponse(
        status_code=404, content={"message": "Habit not found"})
