"""
The users schema file that contains model classes to format user objects
while creating or display to users.

Classes:

    UserBase
    UserCreate
    UserUpdate
    UserShow

Functions:
    None

Misc variables:
    None
"""
import datetime

from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    """
    A class to represent a user base object.
    Defines the required attributes of a user.
    ...

    Attributes
    ----------
    email : str
        the email of a user
    first_name : str
        the first name of a user
    phone_number : str
        the phone number of a user

    Methods
    -------
    None
    """
    email: str
    first_name: str
    phone_number: str


class UserCreate(UserBase):
    """
    A class to format details needed to create a new user.
    Inherits from the UserBase to get the default values.
    ...

    Attributes
    ----------
    password : str
        the password of a user

    Methods
    -------
    None
    """
    password: str


class UserUpdate(UserBase):
    """
    A class to format details needed to create a new user.
    Inherits from the UserCreate to get the default values.
    ...

    Attributes
    ----------
    middle_name: str
        the middle name of a user
    last_name: str
        the user's last name
    dob: str
        the user's date of birth
    nationality:
        the user's nationality/country

    Methods
    -------
    None
    """
    middle_name: str
    last_name: str
    dob: datetime.date
    nationality: str


class UserShow(UserBase):
    """
    A class to format how a user object is returned as json.
    ...

    Attributes
    ----------
    id: int
        the generated user id
    email : str
        the email of a user
    first_name : str
        the first name of a user
    phone_number : str
        the phone number of a user
    dob: str
        the user's date of birth
    nationality: str
        the user's nationality

    Methods
    -------
    None
    """
    id: int
    middle_name: Optional[str]
    last_name: Optional[str]
    dob: Optional[datetime.date]
    nationality: Optional[str]
    time_created: datetime.date

    class Config:
        orm_mode = True


class AddressBase(BaseModel):
    """
    A class to represent a user address base object.
    Defines the required attributes of a user address.
    ...

    Attributes
    ----------
    contry : str
        the user's contry
    city : str
        the user's city
    state : str
        the user's state
    province : str
        the user's province
    zip : int
        the user's zip code

    Methods
    -------
    None
    """
    contry: str
    city: str
    state: str
    province: str
    zip: int


class AddressCreate(AddressBase):
    """
    A class to format details needed to create a new address.
    Inherits from the AddressBase to get the default values.
    ...

    Attributes
    ----------
    user_id : int
        the id of the user creating the address

    Methods
    -------
    None
    """
    user_id: int


class AddressShow(AddressCreate):
    """
    A class to format the user address for display.
    ...

    Attributes
    ----------
    id: int
        the id of the address record
    user_id: int
        the id of the user who created the address
    contry : str
        the user's contry
    city : str
        the user's city
    state : str
        the user's state
    province : str
        the user's province
    zip : int
        the user's zip code

    Methods
    -------
    None
    """
    id: int
    user_id: int
    contry: str
    city: str
    state: str
    province: str
    zip: int
    time_created: datetime.date

    class Config:
        orm_mode = True


class UserDetailsShow(UserShow):
    """
    A class to format how a details user object is returned as json.
    ...

    Attributes
    ----------
    all the profile details for the user

    addresses: all addresses created by the user

    Methods
    -------
    None
    """
    addresses: list[AddressShow]

    class Config:
        orm_mode = True
