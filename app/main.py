from fastapi import FastAPI

from app.routes import demo_routes, user_routes

app = FastAPI(title="Async FastAPI Demo")


app.include_router(demo_routes.router)
app.include_router(user_routes.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Async FastAPI Demo",
        "docs": "/docs",
        "endpoints": [
            "/api/basic-async",
            "/api/sequential",
            "/api/concurrent",
            "/api/users/1/dashboard",
        ],
    }