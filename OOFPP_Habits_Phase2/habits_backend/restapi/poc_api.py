import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/")
async def hello():
    a = "test"
    return {"message": "Hello World"}

uvicorn.run(app, host="0.0.0.0", port=8000)