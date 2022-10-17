"""
The users repository file to contain methods that interact with the database.

Classes:

    None

Functions:

    get_users(skip, limit, db):
        returns existing users list paginated as defined.

Misc variables:

    router:
        the users router object to encapsulate all user module
        endpoint methods.
"""

from sqlalchemy.orm import Session

from app import models


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
    return db.query(models.User).offset(skip).limit(limit).all()
