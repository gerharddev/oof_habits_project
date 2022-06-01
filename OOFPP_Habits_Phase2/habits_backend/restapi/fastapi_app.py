"""
This module provide a REST API for the habit tracking application using FastAPI

Information:
    https://fastapi.tiangolo.com/
    https://fastapi.tiangolo.com/tutorial/sql-databases/

"""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from . import habits, frequencies, completed_habits, analysis, data
from habits_backend.database.connectors import Base, make_engine


def start_api_server():
    """Start the REST API"""

    app = FastAPI()
    Base.metadata.create_all(bind=make_engine())    # Create all database table
    # TODO: Seed testing data

    @app.get("/", tags=["root"])
    def root():
        """Application root. Redirects to the docs page."""
        return RedirectResponse("/docs")

    app.include_router(data.router)
    app.include_router(frequencies.router)
    app.include_router(habits.router)
    app.include_router(completed_habits.router)
    app.include_router(analysis.router)

    uvicorn.run(app, host="0.0.0.0", port=8000)
