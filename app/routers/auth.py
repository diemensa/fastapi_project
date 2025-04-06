from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from app.auth import bcrypt_context, create_access_token, authenticate_user
from app.database import db_dependency
from app.models.user import User
from app.schemes import UserBase, TokenBase

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserBase):
    res = db.query(User).filter(User.username == user_request.name)

    if res.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This username already exists!")

    cr_user_model = User(username=user_request.name,
                         hashed_password=bcrypt_context.hash(user_request.password))

    db.add(cr_user_model)
    db.commit()
    return f"Account {cr_user_model.username} was created!"


@router.post("/token", response_model=TokenBase)
async def login_access_token(form: Annotated[OAuth2PasswordRequestForm, Depends()],
                             db: db_dependency):
    user = authenticate_user(form.username, form.password, db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong username or password")

    token = create_access_token(user.username, user.id, timedelta(minutes=60))

    return {'access_token': token,
            'token_type': 'bearer'}
