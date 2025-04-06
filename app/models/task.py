from app.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    state = Column(String)
    deadline = Column(Date)
    owner_id = Column(Integer, ForeignKey("user.id"))
