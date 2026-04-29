from pydantic import BaseModel
from typing import Any


class DashboardResponse(BaseModel):
    message: str
    user: dict[str, Any]
    total_posts: int
    total_todos: int
    sample_posts: list[dict[str, Any]]
    sample_todos: list[dict[str, Any]]
    time_taken: float