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

from fastapi import FastAPI

from app.users import router as users


app = FastAPI()

app = FastAPI()

app.include_router(router=users.router)


@app.get("/", tags=["Home"])
def show_root():
    """
    Show the welcome message to the API users.
    """
    return {
        "message": "Hello, welcome to the SokoFresh user management API",
    }
