from .database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    state = Column(String)
    deadline = Column(Date)
    owner_id = Column(Integer, ForeignKey("user.id"))
