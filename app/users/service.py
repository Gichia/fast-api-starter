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
