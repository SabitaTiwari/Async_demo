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
            "/api/v1/demo/basic-async",
            "/api/v1/demo/sequential",
            "/api/v1/demo/concurrent",
            "/api/v1/users/1/dashboard",
        ],
    }