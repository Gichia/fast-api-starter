"""
The auth module router to implement authenticationa dn authorization
endpoints.

Including email verfication

Classes:

    None

Functions:

    register_user(first_name, email, password):
        register a new user

Misc variables:

    router:
        the auth router object to encapsulate the auth module endpoints.
"""

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, status

from app import database
from app.value_chains import schema, service
from app.auth.service import get_current_user

get_db = database.get_db

router = APIRouter(
    prefix="/value_chains",
    tags=["Value Chains"],
)


@router.post("",
             status_code=status.HTTP_201_CREATED,
             response_model=schema.ValueChainShow)
async def create_value_chain(
    request: schema.ValueChainBase,
    email=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Create a new value chain

    Parameters:
    ----------
        name: str
            the name of the value chain

    Returns:
    -------
        ValueChain: the newly created value chain
    """
    return await service.create_value_chain(
        db=db, email=email, chain=request)


@router.put("/{chain_id}",
            status_code=status.HTTP_200_OK,
            response_model=schema.ValueChainShow)
async def update_value_chain(
    chain_id: int,
    request: schema.ValueChainBase,
    email=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Update value chain details

    Parameters:
    ----------
        chain_id: int
            the id of the value chain to be updated
        name: str
            the name of the value chain

    Returns:
    -------
        ValueChain: the newly created value chain

    Raises
    ------
        NotFoundError: If the value chain does not exist
    """
    return await service.update_value_chain(
        db=db, email=email, chain_id=chain_id, chain=request)


@router.delete("/{chain_id}", status_code=status.HTTP_200_OK)
async def delete_value_chain(
    chain_id: int,
    email=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Delete user value chain record

    Parameters:
    ----------
        chain_id: int
            the id of the value chain to be deleted 

    Returns:
    -------
        Dict: the success message
    """
    return await service.delete_value_chain(
        db=db, email=email, chain_id=chain_id)
