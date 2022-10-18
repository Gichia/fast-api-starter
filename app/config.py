"""
Config file to setup the app base settings

Classes:

    Settings

Functions:

    None

Misc variables:

    description:
        The base description string for the docs
"""

from pydantic import BaseSettings

description = """
Users Management API to manage user portfolios.
"""


class Settings(BaseSettings):
    """
    The class to setup default variables for the API.

    Attributes
    ----------
    DB_URI: str
        the db uri string.
    APP_NAME : str
        the app name for the API will show up on docs page.
    DESCRIPTION : str
        a detailed description string for docs page.

    Methods
    -------
    None
    """
    DB_URI: str
    SECRET_KEY: str
    FROM_EMAIL: str
    MAILGUN_DOMAIN: str
    MAILGUN_API_KEY: str
    ALGORITHM: str = "HS256"
    DESCRIPTION: str = description
    FROM_TITLE: str = "Farmers API"
    APP_NAME: str = "User Management API"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 59

    class Config:
        env_file = ".env"
