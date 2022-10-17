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
from app.users import schema


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
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


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
        None: if the user is not found.
    """
    user: models.User | None = db.query(models.User).filter(
        models.User.id == user_id).first()

    return user


async def update_user(
        db: Session,
        user_id: int,
        user: schema.UserUpdate
) -> models.User:
    """
    Save updated user details in the database.

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
        User:
            the updated user details
    """
    db.query(models.User).filter(models.User.id ==
                                 user_id).update({**user.dict()},
                                                 synchronize_session=False)
    db.commit()

    return await get_by_id(db=db, user_id=user_id)


async def delete_user(db: Session, user_id: int) -> None:
    """
    Remove user details in the database.

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
    db.query(models.User).filter(models.User.id ==
                                 user_id).delete(synchronize_session=False)
    db.commit()

    return


async def create_address(
        db: Session, address: schema.AddressCreate) -> models.UserAddress:
    """
    Save a new user address to the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        address: (schema.AddressCreate):
            the required address details.

    Returns:
    -------
        UserAddress: the newly created address
    """
    new_address = models.UserAddress(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


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
        None: if the address is not found.
    """
    address: models.UserAddress | None = db.query(models.UserAddress).filter(
        models.UserAddress.id == addr_id).first()

    return address


async def update_address(
        db: Session,
        addr_id: int,
        address: schema.AddressCreate
) -> models.UserAddress:
    """
    Save updated address details in the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        addr_id: int
            the id of the address to be updated
        address: (schema.AddressCreate):
            the updated address details.

    Returns:
    -------
        UserAddress: the updated address details
    """
    db.query(models.UserAddress).filter(
        models.UserAddress.id == addr_id).update(
            {**address.dict()}, synchronize_session=False)

    db.commit()

    return await get_address_by_id(db=db, addr_id=addr_id)


async def delete_address(db: Session, addr_id: int) -> None:
    """
    Remove address details from the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        addr_id: int
            the id of the address to be deleted

    Returns:
    -------
        None
    """
    db.query(models.UserAddress).filter(
        models.UserAddress.id == addr_id).delete(synchronize_session=False)

    db.commit()

    return
