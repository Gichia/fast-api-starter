"""

"""
import pytest

from app.users import repository, schema, service

from app.tests.base_test import db


@pytest.mark.anyio
async def test_repository_crud():
    test_address = schema.AddressCreate(
        city="Nairobi",
        contry="Kenya",
        province="Province",
        state="",
        user_id=1,
        zip=50089,
    )

    update_address = schema.AddressCreate(
        city="Kampala",
        contry="Uganda",
        province="Province",
        state="Uganda",
        user_id=1,
        zip=79689,
    )

    await repository.delete_address(db=db, addr_id=1)

    data = await repository.create_address(db=db, address=test_address)

    assert data.zip == 50089
    assert data.city == "Nairobi"
    assert data.contry == "Kenya"
    assert data.province == "Province"

    addr_data = await repository.get_address_by_id(db=db, addr_id=1)

    assert addr_data.id == 1
    assert addr_data.state == ""
    assert addr_data.user_id == 1
    assert addr_data.zip == 50089
    assert addr_data.city == "Nairobi"
    assert addr_data.contry == "Kenya"
    assert addr_data.province == "Province"

    address = await repository.update_address(
        db=db, addr_id=1, address=update_address)

    assert address.id == 1
    assert address.user_id == 1
    assert address.zip == 79689
    assert address.state == "Uganda"
    assert address.city == "Kampala"
    assert address.contry == "Uganda"
    assert address.province == "Province"

    await repository.delete_address(db=db, addr_id=1)

    data = await repository.get_address_by_id(db=db, addr_id=1)

    assert data is None
