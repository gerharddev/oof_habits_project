"""
This module provide a REST API for the habit tracking application using FastAPI

Information:
    https://fastapi.tiangolo.com/
    https://fastapi.tiangolo.com/tutorial/sql-databases/

"""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from . import habits, frequencies


def start_api_server():
    """Start the REST API"""

    app = FastAPI()

    @app.get("/", tags=["root"])
    def root():
        """Application root. Redirects to the docs page."""
        return RedirectResponse("/docs")

    app.include_router(habits.router)
    app.include_router(frequencies.router)

    uvicorn.run(app, host="0.0.0.0", port=8000)
