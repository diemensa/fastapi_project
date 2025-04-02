from pydantic import BaseModel, FutureDate


class UserBase(BaseModel):
    name: str
    password: str


class TaskBase(BaseModel):
    task: str
    state: str
    deadline: FutureDate


class TokenBase(BaseModel):
    access_token: str
    token_type: str
