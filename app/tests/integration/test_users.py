"""

"""
import pytest

from app.users import repository, schema, service

from app.tests.base_test import db


@pytest.mark.anyio
async def test_user_crud():
    test_user = schema.UserCreate(
        first_name="Test",
        email="test@test.com",
        password="password",
    )

    await repository.delete_user(db=db, user_id=1)

    data = await repository.create_user(db=db, user=test_user)

    assert data.id == 1
    assert data.first_name == "Test"
    assert data.password == "password"
    assert data.email == "test@test.com"

    user_data = await repository.get_by_id(db=db, user_id=1)

    assert user_data.id == 1
    assert user_data.first_name == "Test"
    assert user_data.password == "password"
    assert user_data.email == "test@test.com"

    users = await repository.get_users(db=db)

    assert len(users) == 1

    await repository.delete_user(db=db, user_id=1)

    data = await repository.get_by_id(db=db, user_id=1)

    assert data is None
