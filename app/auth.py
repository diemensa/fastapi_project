from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette import status

from app.models.user import User

SECRET_KEY = "NIEMANDHIERWIRDKENNENOBICHWEISSMONSTERNURIMKUEHLSCHRANKHABE1337"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

router = APIRouter(prefix="/auth", tags=["auth"])


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    if not bcrypt_context.verify(password, user.hashed_password):
        return None

    return user


def create_access_token(username: str, user_id: int, timelimit: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + timelimit
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_cur_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Couldn't validate the user")

        return {'username': username,
                'id': user_id}

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Couldn't validate the user")

