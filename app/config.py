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
    APP_NAME : str
        the app name for the API will show up on docs page.
    DESCRIPTION : str
        a detailed description string for docs page.

    Methods
    -------
    None
    """
    APP_NAME: str = "User Management API"
    DESCRIPTION: str = description

    class Config:
        env_file = ".env"
