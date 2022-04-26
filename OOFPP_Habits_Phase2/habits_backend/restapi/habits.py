"""Habits endpoints"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/habits/", tags=["habits"])
async def read_habits():
    return [{"username": "Rick"}, {"username": "Morty"}]