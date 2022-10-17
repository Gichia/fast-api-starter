"""
The users module router file to contain all endpoints for the users module.

Classes:

    None

Functions:

    get_users(skip, limit):
        returns existing users list paginated as defined.

Misc variables:

    router:
        the users router object to encapsulate all user module
        endpoint methods.
"""

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, status

from app import database
from app.users import service, schema

get_db = database.get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("",
            status_code=status.HTTP_200_OK,
            response_model=list[schema.UserShow])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> list[schema.UserShow]:
    """
    Returns existing users list paginated as defined. 

    Parameters:
    ----------
        skip (int):
            the initial number of users to be skipped for pagination.
        limit (int):
            the number of records to be fetched.

    Returns:
    -------
            list[Users]:
                the app users existing in the db.
    """
    return await service.get_users(db=db, skip=skip, limit=limit)


@router.post("",
             status_code=status.HTTP_201_CREATED,
             response_model=schema.UserShow)
async def create_user(
        request: schema.UserCreate, db: Session = Depends(get_db)):
    """
    Save a new user details to the database.

    Parameters:
    ----------
        email : str
            the email of a user
        first_name : str
            the first name of a user
        phone_number : str
            the phone number of a user
        password : str
            the user's password

    Returns:
    -------
        User:
            the newly created user details
    """
    return await service.create_user(db=db, user=request)


@router.put("/{user_id}",
            status_code=status.HTTP_200_OK,
            response_model=schema.UserShow)
async def update_user(
        user_id: int,
        request: schema.UserUpdate,
        db: Session = Depends(get_db)):
    """
    Update user details.

    Parameters:
    ----------
        email : str
            the email of a user
        first_name : str
            the first name of a user
        phone_number : str
            the phone number of a user
        password : str
            the user's password
        middle_name: str
            the middle name of a user
        last_name: str
            the user's last name
        dob: str
            the user's date of birth
        nationality:
            the user's nationality/country

    Returns:
    -------
        User:
            the updated user details
    """
    return await service.update_user(db=db, user_id=user_id, user=request)
