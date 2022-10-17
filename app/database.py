"""
module file to setup the correct database session that can be
reused depending on the instance initialized.

Classes:

    None

Functions:
    get_db():
        the method to return the correct db session depending
        on the instance.

Misc variables:
    None
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config import Settings


settings = Settings()

SQLALCHEMY_DATABASE_URL = settings.DB_URI

engine = create_engine(url=SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    """
    Returns the current db session depending on the instance.
    Can either be TEST or DEV or LIVE instance.

    Parameters
    ----------
    None

    Returns
    -------
        db: Session
            the database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
