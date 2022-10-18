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
from typing import Dict
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

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


async def get_by_id(db: Session, user_id: int) -> models.User | None:
    """
    Return a user with the provided id if they exist.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        user_id: int
            the id of the user to be fetched

    Returns:
    -------
        User: the user details

    Raises
    ------
        NotFoundError: If the user is not found
    """
    user = await repository.get_by_id(db=db, user_id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{user_id}' not found.")

    return user


async def get_by_email(db: Session, email: str) -> models.User | None:
    """
    Return a user with the provided email if they exist.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the email of the user to be fetched

    Returns:
    -------
        User: the user details

    Raises
    ------
        NotFoundError: If the user is not found
    """
    user = await repository.get_by_email(db=db, email=email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email '{email}' not found.")

    return user


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


async def delete_user(db: Session, user_id: int) -> Dict:
    """
    Implement the endpoint to delete user details.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        user_id: int
            the id of the user to be deleted

    Returns:
    -------
        None
    """
    await repository.delete_user(db=db, user_id=user_id)

    return {"message": "User successfully deleted."}


async def create_address(
        db: Session, address: schema.AddressBase) -> models.UserAddress:
    """
    Implement the endpoint to create a new user address.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        address: (schema.AddressBase):
            the required address details.

    Returns:
    -------
        UserAddress: the newly created address
    """
    user_id = 1
    new_address = schema.AddressCreate(**address.dict(), user_id=user_id)

    return await repository.create_address(db=db, address=new_address)


async def get_address_by_id(
        db: Session, addr_id: int) -> models.UserAddress | None:
    """
    Return user address with the provided id if they exist.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        addr_id: int
            the id of the address

    Returns:
    -------
        UserAddress: the address details

    Raises
    ------
        NotFoundError: If the address is not found
    """
    address = await repository.get_address_by_id(db=db, addr_id=addr_id)

    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Address with id '{addr_id}' not found.")

    return address


async def update_address(
    db: Session,
    addr_id: int,
    address: schema.AddressBase
) -> models.UserAddress:
    """
    Implement the endpoint to update address details.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        address: (schema.AddressBase):
            the required address details.

    Returns:
    -------
        UserAddress: the newly created address

    Raises
    ------
        NotFoundError: If the address is not found
    """
    existing = await get_address_by_id(db=db, addr_id=addr_id)

    upd_address = schema.AddressCreate(
        **address.dict(),
        user_id=existing.user_id,
    )

    return await repository.create_address(db=db, address=upd_address)
