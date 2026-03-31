# test_server.py
import pytest # type: ignore
from src.add_inputs import add_numbers, find_gcd, AddInput

@pytest.mark.asyncio
async def test_add_numbers():
    result = await add_numbers(AddInput(a=2.0, b=3.0))
    assert '"result": 5.0' in result

@pytest.mark.asyncio
async def test_validation_error():
    with pytest.raises(Exception):
        AddInput(a="not_a_number", b=1.0)  # should fail Pydantic validation

@pytest.mark.asyncio
async def test_find_gcd():
    result = await find_gcd(AddInput(a=12.0, b=8.0))
    assert '"result": 4' in result

@pytest.mark.asyncio
async def test_find_gcd_coprime():
    result = await find_gcd(AddInput(a=7.0, b=13.0))
    assert '"result": 1' in result

@pytest.mark.asyncio
async def test_find_gcd_one_zero():
    result = await find_gcd(AddInput(a=5.0, b=0.0))
    assert '"result": 5' in result