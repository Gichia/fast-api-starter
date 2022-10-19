"""

"""
import pytest

from app.value_chains import repository, schema

from app.tests.base_test import db


@pytest.mark.anyio
async def test_repository_crud():
    test_chain = schema.ValueChainCreate(
        name="Avocados",
        user_id=1
    )

    update_chain = schema.ValueChainCreate(
        name="Mangos",
        user_id=1
    )

    await repository.delete_value_chain(db=db, chain_id=1)

    data = await repository.create_value_chain(db=db, chain=test_chain)

    assert data.id == 1
    assert data.name == "Avocados"

    chain_data = await repository.get_by_id(db=db, chain_id=1)

    assert chain_data.id == 1
    assert chain_data.name == "Avocados"

    upd_chain = await repository.update_value_chain(
        db=db, chain_id=1, chain=update_chain)

    assert upd_chain.id == 1
    assert upd_chain.user_id == 1
    assert upd_chain.name == "Mangos"

    await repository.delete_value_chain(db=db, chain_id=1)

    data = await repository.get_by_id(db=db, chain_id=1)

    assert data is None
