import uvicorn

from fastapi import FastAPI
from app.routers import auth, task

app = FastAPI()

app.include_router(auth.router)
app.include_router(task.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)