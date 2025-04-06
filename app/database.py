from app.config import get_db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from fastapi import Depends
from typing import Annotated


DATABASE_URL = get_db_url()
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
