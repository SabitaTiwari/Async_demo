import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.main import app
from app.services.demo_service import (
    get_user_data,
    get_order_data,
    get_notification_data,
)


@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_root_endpoint(async_client):
    response = await async_client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Welcome to Async FastAPI Demo"
    assert data["docs"] == "/docs"
    assert "/api/basic-async" in data["endpoints"]
    assert "/api/sequential" in data["endpoints"]
    assert "/api/concurrent" in data["endpoints"]


@pytest.mark.asyncio
async def test_basic_async_endpoint(async_client):
    response = await async_client.get("/api/basic-async")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "This endpoint waited asynchronously for 2 seconds"
    assert "time_taken" in data


@pytest.mark.asyncio
async def test_get_user_data_service():
    user = await get_user_data()

    assert user["id"] == 1
    assert user["name"] == "Sabita Tiwari"


@pytest.mark.asyncio
async def test_get_order_data_service():
    orders = await get_order_data()

    assert isinstance(orders, list)
    assert len(orders) == 2
    assert orders[0]["item"] == "Keyboard"
    assert orders[1]["item"] == "Mouse"


@pytest.mark.asyncio
async def test_get_notification_data_service():
    notifications = await get_notification_data()

    assert isinstance(notifications, list)
    assert len(notifications) == 2
    assert notifications[0]["message"] == "Your order has been shipped"


@pytest.mark.asyncio
async def test_sequential_endpoint(async_client):
    response = await async_client.get("/api/sequential")

    assert response.status_code == 200

    data = response.json()

    assert data["type"] == "Sequential async"
    assert data["user"]["name"] == "Sabita Tiwari"
    assert len(data["orders"]) == 2
    assert len(data["notifications"]) == 2
    assert "time_taken" in data


@pytest.mark.asyncio
async def test_concurrent_endpoint(async_client):
    response = await async_client.get("/api/concurrent")

    assert response.status_code == 200

    data = response.json()

    assert data["type"] == "Concurrent async"
    assert data["user"]["name"] == "Sabita Tiwari"
    assert len(data["orders"]) == 2
    assert len(data["notifications"]) == 2
    assert "time_taken" in data


@pytest.mark.asyncio
async def test_concurrent_is_faster_than_sequential(async_client):
    sequential_response = await async_client.get("/api/sequential")
    concurrent_response = await async_client.get("/api/concurrent")

    assert sequential_response.status_code == 200
    assert concurrent_response.status_code == 200

    sequential_time = sequential_response.json()["time_taken"]
    concurrent_time = concurrent_response.json()["time_taken"]

    assert concurrent_time < sequential_time