"""
The users service file to implement user endpoints functionalities.

Classes:

    None

Functions:

    get_users(skip, limit, db):
        returns existing users from the repository.

Misc variables:

    None
"""
from sqlalchemy.orm import Session

from app import models
from app.users import schema, repository


async def get_users(
        db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    """
    Returns existing users in the db list paginated as defined. 

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        skip (int):
            the initial number of users to be skipped for pagination.
        limit (int):
            the number of records to be fetched.

    Returns:
    -------
            list[User]:
                the app users existing in the db.
    """
    return await repository.get_users(db=db, skip=skip, limit=limit)


async def create_user(
        db: Session, user: schema.UserCreate) -> models.User:
    """
    Save a new user details to the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        user: (schema.UserCreate):
            the default user details.

    Returns:
    -------
        User:
            the newly created user details
    """
    return await repository.create_user(db=db, user=user)


async def update_user(
        db: Session,
        user_id: int,
        user: schema.UserUpdate
) -> models.User:
    """
    Implement endpoint to update user details.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        user_id: int
            the id of the user to be updated
        user: (schema.UserUpdate):
            the updated user details.

    Returns:
    -------
        User: the updated user details
    """
    return await repository.update_user(db=db, user_id=user_id, user=user)
