"""
Create the base app object that will import all routes and
application models during initialization

Classes:

    None

Functions:

    show_root():
        returns the welcome message for the API.

Misc variables:

    app:
        the base fast api object from the FastAPI class
"""
from functools import lru_cache

from fastapi import FastAPI, Depends

from app import models
from app.database import engine
from app.config import Settings
from app.auth import router as auth
from app.users import router as users


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()

app = FastAPI(title=settings.APP_NAME, description=settings.DESCRIPTION)

app = FastAPI()

app.include_router(router=auth.router)
app.include_router(router=users.router)

models.Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Home"])
def show_root(settings: Settings = Depends(get_settings)):
    """
    Show the welcome message to the API users.
    """
    return {
        "message": f"Hello, welcome to the {settings.APP_NAME}",
    }
