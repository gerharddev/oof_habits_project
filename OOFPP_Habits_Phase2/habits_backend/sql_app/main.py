
# """
# This module provide a REST API for the habit tracking application using FastAPI
#
# Information:
#     https://fastapi.tiangolo.com/
#     https://fastapi.tiangolo.com/tutorial/sql-databases/
#
# """

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from . import models
from .database import SessionLocal, engine
from habits_backend.restapi import habits, frequencies

def start_api_server():
    """Start the REST API"""
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()

    # Dependency
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @app.get("/", tags=["root"])
    def root():
        """Application root. Redirects to the docs page."""
        return RedirectResponse("/docs")

    # @app.get("/frequencies/", response_model=list[schemas.Frequency])
    # async def read_frequencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    #     frequencies = crud.get_frequencies(db, skip=skip, limit=limit)
    #     return frequencies
    #
    # @app.post("/frequencies/", response_model=schemas.Frequency)
    # async def create_frequency(frequency: schemas.FrequencyCreate, db: Session = Depends(get_db)):
    #     db_frequency = crud.get_frequency_by_name(db, name=frequency.name)
    #     if db_frequency:
    #         raise HTTPException(status_code=400, detail="Frequency already exist")
    #     return crud.create_frequency(db=db, frequency=frequency)

    app.include_router(habits.router)
    app.include_router(frequencies.router)

    uvicorn.run(app, host="0.0.0.0", port=8000)







#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
