"""
The value chain schema file that contains model classes to format
value_chain objects while creating or display.

Classes:

    ValueChainBase
    ValueChainCreate
    ValueChainShow

Functions:
    None

Misc variables:
    None
"""
import datetime

from typing import Optional
from pydantic import BaseModel


class ValueChainBase(BaseModel):
    """
    A class to represent a value_chain base object.
    Defines the required attributes for a value chain.
    ...

    Attributes
    ----------
    name : str
        the name of the value chain

    Methods
    -------
    None
    """
    name: str


class ValueChainCreate(ValueChainBase):
    """
    A class to format details needed to create a new value chain.
    Inherits from the ValueChainBase to get the default values.
    ...

    Attributes
    ----------
    user_id : int
        the id of the user adding the value chain

    Methods
    -------
    None
    """
    user_id: int


class ValueChainShow(ValueChainCreate):
    """
    A class to format how a value chain object is returned as json.
    ...

    Attributes
    ----------
    id: int
        the generated  id
    name : str
        the name of the value chain
    user_id: int
        the id of the user who created the value chain
    time_created: str
        the date it was created

    Methods
    -------
    None
    """
    id: int
    name: str
    user_id: int
    time_created: datetime.date

    class Config:
        orm_mode = True
