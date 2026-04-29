import asyncio


async def get_user_data():
    await asyncio.sleep(2)
    return {
        "id": 1,
        "name": "Sabita Tiwari",
    }


async def get_order_data():
    await asyncio.sleep(2)
    return [
        {"id": 101, "item": "Keyboard"},
        {"id": 102, "item": "Mouse"},
    ]


async def get_notification_data():
    await asyncio.sleep(2)
    return [
        {"id": 1, "message": "Your order has been shipped"},
        {"id": 2, "message": "New login detected"},
    ]