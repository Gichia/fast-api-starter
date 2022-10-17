"""
Test the root api endpoint and make sure
application is initialized correctly
"""

from fastapi.testclient import TestClient

from app.config import Settings
from app.main import app, get_settings


client = TestClient(app=app)


def get_settings_override():
    return Settings(APP_NAME="Users API")


app.dependency_overrides[get_settings] = get_settings_override


def test_root():
    """
    Test the root endpoint to ensure it has a welcome message property.

    Ensure the APP default variables are correctly initialized.
    """
    response = client.get(url="/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "message" in data
