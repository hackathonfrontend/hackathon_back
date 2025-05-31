from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.database import create_tables
from app.routers import user_router # Or your specific router module
from app.routers import manga_room_router # Add this import
from app.routers import creation_story_router
from app.routers import member_router
from app.routers import notification_router
from app.routers import prompt_router
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database and create tables
    create_tables()
    yield
    # Here you can add any cleanup code if necessary, like closing connections
    # For example: await close_database_connections()

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
app.include_router(user_router.router)
app.include_router(manga_room_router.router) # Add this line
app.include_router(creation_story_router.router)
app.include_router(member_router.router)
app.include_router(notification_router.router)
app.include_router(prompt_router.router)