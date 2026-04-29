import asyncio
import time

import httpx
from fastapi import APIRouter, HTTPException

from app.core.config import (
    REQUEST_TIMEOUT_SECONDS,
    HTTP_CLIENT_TIMEOUT_SECONDS,
)
from app.schemas.dashboard_schema import DashboardResponse
from app.services.external_api_service import fetch_json

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)


@router.get("/{user_id}/dashboard", response_model=DashboardResponse)
async def user_dashboard(user_id: int):
    start_time = time.perf_counter()

    try:
        async with asyncio.timeout(REQUEST_TIMEOUT_SECONDS):
            async with httpx.AsyncClient(timeout=HTTP_CLIENT_TIMEOUT_SECONDS) as client:
                user, posts, todos = await asyncio.gather(
                    fetch_json(client, f"/users/{user_id}"),
                    fetch_json(client, f"/users/{user_id}/posts"),
                    fetch_json(client, f"/users/{user_id}/todos"),
                )

    except TimeoutError:
        raise HTTPException(
            status_code=504,
            detail="Request took too long",
        )

    end_time = time.perf_counter()

    return {
        "message": "User dashboard loaded using async concurrent API calls",
        "user": user,
        "total_posts": len(posts),
        "total_todos": len(todos),
        "sample_posts": posts[:3],
        "sample_todos": todos[:3],
        "time_taken": round(end_time - start_time, 2),
    }