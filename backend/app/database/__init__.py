from typing import Generator

from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db(request: Request) -> Generator[Session, None, None]:
    """
    Get a database session.

    Args:
        request (fastapi.Request): The request object.

    Yields:
        sqlalchemy.orm.Session: A database session.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()

from ..models import *  # noqa

Base.metadata.create_all(bind=engine)
