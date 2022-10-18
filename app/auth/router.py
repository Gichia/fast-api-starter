"""
The auth module router to implement authenticationa dn authorization
endpoints.

Including email verfication

Classes:

    None

Functions:

    register_user(first_name, email, password):
        register a new user

Misc variables:

    router:
        the auth router object to encapsulate the auth module endpoints.
"""

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, status

from app import database
from app.users import service, schema

get_db = database.get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register",
             status_code=status.HTTP_201_CREATED,
            #  response_model=schema.UserShow
             )
async def register_user(
        request: schema.UserCreate, db: Session = Depends(get_db)):
    """
    Save a new user details to the database.

    Parameters:
    ----------
        email : str
            the email of a user
        first_name : str
            the first name of a user
        password : str
            the user's password

    Returns:
    -------
        User: the newly created user details
    """
    return "Hello"