# Async FastAPI Demo

This is a demo FastAPI project created to understand asynchronous programming in Python.

## Features

- FastAPI clean project structure
- Async routes using `async def`
- Async waiting using `await`
- Sequential async demo
- Concurrent async demo using `asyncio.gather`
- External API calls using `httpx.AsyncClient`
- Timeout handling using `asyncio.timeout`
- Clean separation of routes, services, schemas, and core config

## Project Structure

```text
app/
├── main.py
├── core/
│   └── config.py
│─── routes/
│      ├── demo_routes.
│      └── user_routes.
├── services/
│   ├── demo_service.py
│   ├── external_api_service.py
│   └── user_service.py
└── schemas/
    └── dashboard_schema.py

    Installation
python -m venv venv
Activate virtual environment

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Run Project
uvicorn app.main:app --reload
API Docs

After running the project, open:

http://127.0.0.1:8000/docs