from app.database import Base
from sqlalchemy import Column, Integer, String

Base.metadata.clear()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
