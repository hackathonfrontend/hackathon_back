
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.database import create_tables
from app.routers import user_router # Or your specific router module
from app.routers import ai_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database and create tables
    create_tables()
    yield
    # Here you can add any cleanup code if necessary, like closing connections
    # For example: await close_database_connections()

app = FastAPI(lifespan=lifespan)
app.include_router(user_router.router)
app.include_router(ai_router.router)
