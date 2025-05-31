
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.database import create_tables
<<<<<<< HEAD
from app.routers.user_router import router as user_router
=======
from app.routers import user_routers # Or your specific router module
>>>>>>> main

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database and create tables
    create_tables()
    yield
    # Here you can add any cleanup code if necessary, like closing connections
    # For example: await close_database_connections()

app = FastAPI(lifespan=lifespan)
<<<<<<< HEAD
app.include_router(user_router)
=======

app.include_router(user_routers.router)
>>>>>>> main
