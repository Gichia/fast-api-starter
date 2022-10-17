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
