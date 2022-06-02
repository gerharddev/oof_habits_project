"""Completed Habits endpoints"""

from fastapi import APIRouter
import habits_backend.schemas.completed_habits as schemas
from habits_backend.database.connectors import *
from habits_backend.services.completed_habits import completed_habits_service
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/completed-habits",
    tags=["completed-habits"],
    responses={404: {"description": "Not found"}})


@router.get("", response_model=list[schemas.CompletedHabitQuery])
async def get_all(skip: int = 0, limit: int = 100):
    completed_habits = completed_habits_service.get_all(skip=skip, limit=limit)

    return completed_habits


@router.get("/{habit-id}", response_model=list[schemas.CompletedHabitQuery])
async def get_by_habit_id(habit_id, skip: int = 0, limit: int = 100):
    completed_habits = completed_habits_service.get_by_id(habit_id, skip=skip, limit=limit)

    return (completed_habits if completed_habits is not None else JSONResponse(status_code=404,
            content={"message": "Nothing found for this habit id"}))


@router.get("/{habit-id}/detailed", response_model=list[schemas.CompletedHabit])
async def get_by_habit_id_detailed(habit_id, skip: int = 0, limit: int = 100):
    completed_habit = completed_habits_service.get_by_id_detailed(habit_id, skip=skip, limit=limit)

    return completed_habit


@router.post("", response_model=schemas.CompletedHabit)
async def create_completed_habit(completed_habit: schemas.CompletedHabitCreate):
    results = completed_habits_service.create(completed_habit=completed_habit)

    return (JSONResponse(status_code=400, content={"message": "Duplicate - Not inserted"}) if results is "Duplicate"
            else JSONResponse(status_code=200, content={"message": "Completed habit inserted"}))


@router.delete("/{id}")
async def deleted_completed_habit(id: int):
    deleted = completed_habits_service.delete(id=id)

    return JSONResponse(status_code=200, content={"message": "Deleted"}) if deleted is not None else JSONResponse(
        status_code=404, content={"message": "Completed habit not found"})

