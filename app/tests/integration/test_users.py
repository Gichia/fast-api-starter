"""

"""
import pytest
import fastapi

from app.users import repository, schema, service

from app.tests.base_test import db


@pytest.mark.anyio
async def test_repository_crud():
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


@pytest.mark.anyio
async def test_service_crud():
    test_user = schema.UserCreate(
        first_name="Test",
        email="test@test.com",
        password="password",
    )

    update_user = schema.UserUpdate(
        first_name="Test",
        email="test@test.com",
        password="password",
        last_name="Doe",
        middle_name="Test",
        phone_number="2547XXXXXX",
        dob="2020-07-10",
        nationality="",
    )

    await repository.delete_user(db=db, user_id=1)

    data = await service.create_user(db=db, user=test_user)

    assert data.id == 1
    assert data.first_name == "Test"
    assert data.password == "password"
    assert data.email == "test@test.com"

    user_data = await service.get_by_id(db=db, user_id=1)

    assert user_data.id == 1
    assert user_data.first_name == "Test"
    assert user_data.password == "password"
    assert user_data.email == "test@test.com"
    assert user_data.last_name is None
    assert user_data.phone_number is None

    user_data = await service.update_user(
        db=db, email=user_data.email, user=update_user)

    assert user_data.dob is not None
    assert user_data.last_name == "Doe"
    assert user_data.middle_name == "Test"
    assert user_data.phone_number == "2547XXXXXX"

    users = await service.get_users(db=db)

    assert len(users) == 1

    await service.delete_user(db=db, email=data.email)

    data = await service.get_users(db=db)

    assert len(data) == 0

    with pytest.raises(fastapi.exceptions.HTTPException):
        await service.get_by_id(db=db, user_id=1)
