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
from fastapi import HTTPException, status

from app import models
from app.users import schema, service, repository


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

    return await service.create_user(db=db, user=user)
