
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.database import create_tables
from app.routers.user_router import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)