import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_create_statistic():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        test_json = {"views": 100, "clicks": 200, "rub_cost": 8, "cost_per_click": 10}
        response = await ac.post("/statistics", json=test_json)
        assert response.status_code == 200
        assert test_json["views"] == response.json()["views"]
        assert test_json["clicks"] == response.json()["clicks"]
        assert test_json["rub_cost"] == response.json()["rub_cost"]
