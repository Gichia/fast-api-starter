"""
The auth service file to implement auth endpoints functionalities.

Classes:

    None

Functions:

    register_user(db, first_name, email, password):
        register new user details.

Misc variables:

    None
"""
from typing import Dict
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException, status

from app import models
from app.users import schema, service, repository


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password_hash(password: str) -> str:
    """
    Return a password hash

    Parameters:
    ----------
        password: str:
            the password to be hashed.

    Returns:
    -------
        hashed_password:
            the hashed password
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Method to verify if passwords match

    Parameters:
    ----------
        plain_password: str:
            the plain text password.
        hashed_password: str
            the hashed password

    Returns:
    -------
        bool: True if the password match False if not
    """
    return pwd_context.verify(plain_password, hashed_password)


async def register_user(
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
    existing_user = await repository.get_by_email(db=db, email=user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="That email is already in use",
        )

    hashed_password = create_password_hash(password=user.password)
    user.password = hashed_password

    return await service.create_user(db=db, user=user)
