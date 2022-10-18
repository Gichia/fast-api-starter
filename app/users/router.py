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
from app.auth.service import get_current_user

get_db = database.get_db

router = APIRouter(
    prefix="/users",
    dependencies=[Depends(get_current_user)],
)


@router.get("",
            tags=["Users"],
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


@router.get("/{user_id}",
            tags=["Users"],
            status_code=status.HTTP_200_OK,
            response_model=schema.UserDetailsShow)
async def get_user(
        user_id: int,
        db: Session = Depends(get_db)):
    """
    Get user details.

    Parameters:
    ----------
        user_id: the id of the user to be fetched

    Returns:
    -------
        User: the user details if they exist

    Raises
    ------
        NotFoundError: If the user does not exist
    """
    return await service.get_by_id(db=db, user_id=user_id)


@router.put("",
            tags=["Users"],
            status_code=status.HTTP_200_OK,
            response_model=schema.UserShow)
async def update_user(
        request: schema.UserUpdate,
        email=Depends(get_current_user),
        db: Session = Depends(get_db)):
    """
    Update user details.

    Parameters:
    ----------
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
    return await service.update_user(db=db, email=email, user=request)


@router.delete("", tags=["Users"], status_code=status.HTTP_200_OK)
async def delete_user(
        email=Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Delete user details.

    Parameters:
    ----------
        None

    Returns:
    -------
        Dict: the success message
    """
    return await service.delete_user(db=db, email=email)


@router.post("/address",
             tags=["Address"],
             status_code=status.HTTP_201_CREATED,
             response_model=schema.AddressShow)
async def create_address(
        request: schema.AddressBase, db: Session = Depends(get_db)):
    """
    Save a user address details to the database.

    Parameters:
    ----------
        contry : str
            the user's contry
        city : str
            the user's city
        state : str
            the user's state
        province : str
            the user's province
        zip : int
            the user's zip code

    Returns:
    -------
        Address: the newly created address
    """
    return await service.create_address(db=db, address=request)
