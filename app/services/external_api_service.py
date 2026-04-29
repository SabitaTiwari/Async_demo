import httpx
from fastapi import HTTPException

from app.core.config import BASE_URL


async def fetch_json(client: httpx.AsyncClient, endpoint: str):
    try:
        response = await client.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail=f"External API error: {error.response.text}",
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="External service is not available",
        )