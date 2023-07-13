import asyncio
import pytest
from httpx import AsyncClient

from app.networking import app
from app.db import connect_and_init_db, close_db_connect


@pytest.mark.asyncio
async def test_get_all_readings():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await connect_and_init_db()
        response = await ac.get("/readings/")
        await close_db_connect()
    readings = response.json()
    assert response.status_code == 200
    assert len(readings) == 1
    assert readings[0]["session_id"] == -10
    assert readings[0]["timestamp"] == 0    
    