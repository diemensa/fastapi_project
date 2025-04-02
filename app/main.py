import uvicorn

from fastapi import FastAPI
from core.database import engine, Base
from routers.task import router as task_router
from routers.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(task_router)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8080)