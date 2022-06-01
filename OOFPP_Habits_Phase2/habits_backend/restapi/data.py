"""Frequencies endpoints"""

from fastapi import APIRouter
from habits_backend.services.data import data_service
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "Not found"}})


@router.post("/seed")
async def data_seed():
    data_service.sample_data()
    return JSONResponse(status_code=200, content={"message": "Loaded the data"})


@router.delete("/clear")
async def data_delete():
    data_service.clear_database()
    return JSONResponse(status_code=200, content={"message": "Deleted"})
