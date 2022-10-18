"""
The value chain repository file to contain
methods that interact with the database.

Classes:

    None

Functions:

    create_value_chain():
        create a new value chain for a user

Misc variables:

    None
"""

from sqlalchemy.orm import Session

from app import models
from app.value_chains import schema


async def create_value_chain(
        db: Session,
        chain: schema.ValueChainCreate) -> models.ValueChain:
    """
    Save a new value chain details to the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        chain: (schema.ValueChainCreate):
            the new value chain details.

    Returns:
    -------
        ValueChain:
            the newly created value chain
    """
    new_chain = models.ValueChain(**chain.dict())
    db.add(new_chain)
    db.commit()
    db.refresh(new_chain)
    return new_chain


async def get_by_id(db: Session, chain_id: int) -> models.ValueChain | None:
    """
    Return a value_chain with the provided id if they exist.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        chain_id: int
            the id of the value_chain to be fetched

    Returns:
    -------
        ValueChain: the value_chain details
        None: if the value_chain is not found.
    """
    chain: models.ValueChain | None = db.query(models.ValueChain).filter(
        models.ValueChain.id == chain_id).first()

    return chain


async def update_value_chain(
        db: Session,
        chain_id: int,
        chain: schema.ValueChainCreate
) -> models.ValueChain:
    """
    Save updated value chain details in the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        chain_id: int
            the id of the value chain to be updated
        chain: (schema.ValueChainCreate):
            the updated value chain details.

    Returns:
    -------
        ValueChain:
            the updated value chain details
    """
    db.query(models.ValueChain).filter(
        models.ValueChain.id == chain_id).update({
            **chain.dict()}, synchronize_session=False)

    db.commit()

    return await get_by_id(db=db, chain_id=chain_id)


async def delete_value_chain(db: Session, chain_id: int) -> None:
    """
    Remove value chain details from the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        chain_id: int
            the id of the value chain to be deleted

    Returns:
    -------
        None
    """
    db.query(models.ValueChain).filter(
        models.ValueChain.id == chain_id).delete(synchronize_session=False)

    db.commit()

    return
