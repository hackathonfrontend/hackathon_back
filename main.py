
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)