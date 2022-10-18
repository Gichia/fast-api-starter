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
from app.confirmations import CONFIRMATIONS
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
        email: str,
        user: schema.UserUpdate
) -> models.User:
    """
    Implement endpoint to update user details.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email
        user: (schema.UserUpdate):
            the updated user details.

    Returns:
    -------
        User: the updated user details
    """
    current_user = await get_by_email(db=db, email=email)

    return await repository.update_user(
        db=db, user_id=current_user.id, user=user)


async def confirm_user(
        db: Session, user_id: str, passcode: int) -> models.User:
    """
    Implement endpoint to confirm user email.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        passcode: int
            the passcode provided by the user
        user_id: int
            the user id to be confirmed

    Returns:
    -------
        User: the updated user details
    """
    user = await get_by_id(db=db, user_id=user_id)
    print(CONFIRMATIONS)

    is_true = next((
        i for i in CONFIRMATIONS if i["user_email"] == user.email), None)


    if not is_true or is_true["passcode"] != passcode:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The passcode provided is inaccurate.")

    return await repository.confirm_user(db=db, user_id=user_id)


async def delete_user(db: Session, email: str) -> Dict:
    """
    Implement the endpoint to delete user details.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email

    Returns:
    -------
        None
    """
    current_user = await get_by_email(db=db, email=email)

    await repository.delete_user(db=db, user_id=current_user.id)

    return {"message": "User successfully deleted."}


async def create_address(
        db: Session,
        email: str,
        address: schema.AddressBase,
) -> models.UserAddress:
    """
    Implement the endpoint to create a new user address.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email
        address: (schema.AddressBase):
            the required address details.

    Returns:
    -------
        UserAddress: the newly created address
    """
    current_user = await get_by_email(db=db, email=email)

    new_address = schema.AddressCreate(
        **address.dict(), user_id=current_user.id)

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
    email: str,
    addr_id: int,
    address: schema.AddressBase
) -> models.UserAddress:
    """
    Implement the endpoint to update address details.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email
        addr_id: int
            the id of the address to be updated
        address: (schema.AddressBase):
            the required address details.

    Returns:
    -------
        UserAddress: the newly created address

    Raises
    ------
        NotFoundError: If the address is not found
    """
    current_user = await get_by_email(db=db, email=email)

    existing = await get_address_by_id(db=db, addr_id=addr_id)

    if current_user.id != existing.user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address not found.")

    upd_address = schema.AddressCreate(
        **address.dict(),
        user_id=existing.user_id,
    )

    return await repository.update_address(
        db=db, addr_id=addr_id, address=upd_address)


async def delete_address(db: Session, email: str, addr_id: int) -> Dict:
    """
    Implement the endpoint to delete address.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email
        addr_id: int
            the id of the address to be deleted

    Returns:
    -------
        Dict: the success message

    Raises
    ------
        NotFoundError:
            If the address is not found or does not belong to loggedin user
    """
    current_user = await get_by_email(db=db, email=email)

    existing = await get_address_by_id(db=db, addr_id=addr_id)

    if current_user.id != existing.user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address not found.")

    await repository.delete_address(db=db, addr_id=addr_id)

    return {"message": "The address has been successfully deleted"}
