"""
The value chain service file to implement endpoints functionalities.

Classes:

    None

Functions:

    create_value_chain():
        create a new value chain for a user

Misc variables:

    None
"""
from typing import Dict
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app import models
from app.users import service as user_service
from app.value_chains import schema, repository


async def create_value_chain(
        db: Session,
        email: str,
        chain: schema.ValueChainBase,
) -> models.ValueChain:
    """
    Implement the endpoint to create a new value chain.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email
        chain: (schema.ValueChainBase):
            the required value chain details.

    Returns:
    -------
        ValueChain: the newly created value chain
    """
    current_user = await user_service.get_by_email(db=db, email=email)

    new_chain = schema.ValueChainCreate(
        **chain.dict(), user_id=current_user.id)

    return await repository.create_value_chain(db=db, chain=new_chain)


async def get_by_id(
        db: Session, chain_id: int) -> models.ValueChain | None:
    """
    Return value chain with the provided id if they exist.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        chain_id: int
            the id of the value chain

    Returns:
    -------
        ValueChain: the value chain details

    Raises
    ------
        NotFoundError: If the value chain is not found
    """
    value_chain = await repository.get_by_id(db=db, chain_id=chain_id)

    if not value_chain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Value chain with id '{chain_id}' not found.")

    return value_chain


async def update_value_chain(
    db: Session,
    email: str,
    chain_id: int,
    chain: schema.ValueChainBase
) -> models.ValueChain:
    """
    Implement the endpoint to update value chain details.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email
        chain_id: int
            the id of the value chain to be updated
        chain: (schema.ValueChainBase):
            the required value chain details.

    Returns:
    -------
        ValueChain: the updated value chain

    Raises
    ------
        NotFoundError: If the value chain is not found
    """
    current_user = await user_service.get_by_email(db=db, email=email)

    existing = await get_by_id(db=db, chain_id=chain_id)

    if current_user.id != existing.user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Value chain not found.")

    upd_chain = schema.ValueChainCreate(
        **chain.dict(),
        user_id=existing.user_id,
    )

    return await repository.update_value_chain(
        db=db, chain_id=chain_id, chain=upd_chain)


async def delete_value_chain(db: Session, email: str, chain_id: int) -> Dict:
    """
    Implement the endpoint to delete a value chain.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        email: str
            the logged in user email
        chain_id: int
            the id of the value chain to be updated

    Returns:
    -------
        Dict: the success message

    Raises
    ------
        NotFoundError:
            If the value chain is not found
            or it does not belong to loggedin user
    """
    current_user = await user_service.get_by_email(db=db, email=email)

    existing = await get_by_id(db=db, chain_id=chain_id)

    if current_user.id != existing.user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Value chain not found.")

    await repository.delete_value_chain(db=db, chain_id=chain_id)

    return {"message": "The value chain has been successfully deleted"}
