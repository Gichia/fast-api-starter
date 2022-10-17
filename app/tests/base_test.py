"""
Creates the base test to be used as a starting point for all
integration tests.

This should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.

Classes:
--------
    None

Functions:
----------
    override_get_db():
        overrides the default db session with the test instance

Misc Variables:
--------------
    SQLALCHEMY_DATABASE_URL: str
        the default test db url
    engine: Session
        the test db session
"""
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = sqlalchemy.create_engine(
    url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

db = TestingSessionLocal()
client = TestClient(app=app)
