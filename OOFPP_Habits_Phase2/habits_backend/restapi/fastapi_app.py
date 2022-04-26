# """
# This module provide a REST API for the habit tracking application using FastAPI
#
# Information:
#     https://fastapi.tiangolo.com/
#     https://fastapi.tiangolo.com/tutorial/sql-databases/
#
# """

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from habits_backend.sql_app import crud, models, schemas
from habits_backend.sql_app.database import SessionLocal, engine
from habits_backend.database.connectors import *
from . import habits

def start_api_server():
    """Start the REST API"""
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()

    app.include_router(habits.router)

    @app.get("/")
    def root():
        """Application root. Redirects to the docs page."""
        return RedirectResponse("/docs")

    @app.get("/frequencies/", response_model=list[schemas.Frequency])
    async def read_frequencies(skip: int = 0, limit: int = 100):
        with get_db() as session:
            frequencies = crud.get_frequencies(session, skip=skip, limit=limit)

        return frequencies

    # @app.post("/frequencies/", response_model=schemas.Frequency)
    # async def create_frequency(frequency: schemas.FrequencyCreate, db: Session = Depends(get_db)):
    #     db_frequency = crud.get_frequency_by_name(db, name=frequency.name)
    #     if db_frequency:
    #         raise HTTPException(status_code=400, detail="Frequency already exist")
    #     return crud.create_frequency(db=db, frequency=frequency)

    uvicorn.run(app, host="0.0.0.0", port=8000)