"""
module file to setup all app tables

Classes:

    User

Functions:
    None

Misc variables:
    None
"""
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, String, Date, Boolean, ForeignKey, DateTime)

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    dob = Column(Date)
    phone_number = Column(String)
    nationality = Column(String)
    confirmed = Column(Boolean, default=False)
    policy_agreed = Column(Boolean, default=False)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, onupdate=func.now())

    addresses = relationship("UserAddress", back_populates="creator")
    value_chains = relationship("ValueChain", back_populates="creator")


class UserAddress(Base):
    __tablename__ = "user_address"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    contry = Column(String)
    city = Column(String)
    state = Column(String)
    province = Column(String)
    zip = Column(Integer)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, onupdate=func.now())

    creator = relationship("User", back_populates="addresses")


class ValueChain(Base):
    __tablename__ = "value_chain"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, onupdate=func.now())

    creator = relationship("User", back_populates="value_chains")
