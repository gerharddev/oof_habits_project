"""
This module provide a REST API for the habit tracking application using FastAPI

Information:
    https://fastapi.tiangolo.com/

"""
# import uvicorn
# from fastapi import FastAPI
#
# def start_api_server():
#     """Start the REST API"""
#     app = FastAPI()
#
#     @app.get("/")
#     async def root():
#         return {"message": "Hello World"}
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)