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
from app.database import Base
from sqlalchemy import (
    Column, Integer, String, Date, Boolean, ForeignKey, DateTime)


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
    modifierid = Column(Integer, ForeignKey("users.id"))
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, onupdate=func.now())
