import asyncio
import time

from fastapi import APIRouter

from app.services.demo_service import (
    get_user_data,
    get_order_data,
    get_notification_data,
)

router = APIRouter(
    prefix="/api",
    tags=["Async Demo"],
)


@router.get("/basic-async")
async def basic_async():
    start_time = time.perf_counter()

    await asyncio.sleep(2)

    end_time = time.perf_counter()

    return {
        "message": "This endpoint waited asynchronously for 2 seconds",
        "time_taken": round(end_time - start_time, 2),
    }


@router.get("/sequential")
async def sequential_demo():
    start_time = time.perf_counter()

    user = await get_user_data()
    orders = await get_order_data()
    notifications = await get_notification_data()

    end_time = time.perf_counter()

    return {
        "type": "Sequential async",
        "explanation": "Each task waits for the previous task to finish",
        "user": user,
        "orders": orders,
        "notifications": notifications,
        "time_taken": round(end_time - start_time, 2),
    }


@router.get("/concurrent")
async def concurrent_demo():
    start_time = time.perf_counter()

    user, orders, notifications = await asyncio.gather(
        get_user_data(),
        get_order_data(),
        get_notification_data(),
    )

    end_time = time.perf_counter()

    return {
        "type": "Concurrent async",
        "explanation": "All tasks run together during the same waiting period using asyncio.gather",
        "user": user,
        "orders": orders,
        "notifications": notifications,
        "time_taken": round(end_time - start_time, 2),
    }


@router.get("/bad-blocking")
async def bad_blocking():
    import time as blocking_time

    start_time = blocking_time.perf_counter()

    blocking_time.sleep(5)

    end_time = blocking_time.perf_counter()

    return {
        "message": "This is bad because time.sleep blocks the event loop",
        "time_taken": round(end_time - start_time, 2),
    }