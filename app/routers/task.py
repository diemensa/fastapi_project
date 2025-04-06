from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from starlette import status

from app.auth import get_cur_user
from app.database import db_dependency
from app.models.task import Task
from app.schemes import TaskBase

from sqlalchemy import and_

user_dependency = Annotated[str, Depends(get_cur_user)]

router = APIRouter(prefix="/task", tags=["task"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(new_task: TaskBase,
                      db: db_dependency,
                      user: user_dependency):

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Couldn't validate user")

    db_task = Task(task=new_task.task,
                   state=new_task.state,
                   deadline=new_task.deadline,
                   owner_id=user['id'])

    db.add(db_task)
    db.commit()

    return f"Task '{new_task.task}' added!"


@router.delete("/")
async def delete_task(del_task: str,
                      user: user_dependency,
                      db: db_dependency):

    res = db.query(Task).filter(and_(Task.task == del_task,
                                     Task.owner_id == user['id']))

    if not res.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No such task is in the list")

    res.delete()
    db.commit()
    return f'{del_task} was removed from task-list'


@router.get("/")
async def get_task(user: user_dependency,
                   db: db_dependency):

    res = db.query(Task).filter(Task.owner_id == user['id'])

    if not res.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Your To-Do list is empty :(")

    return res.all()
