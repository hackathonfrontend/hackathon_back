import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

# Adjust the import path to your main FastAPI app instance
from main import app
from app.services.prompt_service import PromptService
from app.services.manga_room_service import MangaRoomService
from app.services.creation_story_service import CreationStoryService
from app.services.member_service import MemberService
from app.services.notification_service import NotificationService
from app.services.user_service import UserService # Assuming you have this
from config.dependencies import (
    get_prompt_service,
    get_manga_room_service,
    get_creation_story_service,
    get_member_service,
    get_notification_service,
    get_user_service # Assuming you have this
)

# Fixture for a synchronous TestClient
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

# Fixture for an asynchronous AsyncClient (if you have async endpoints or prefer async tests)
@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

# --- Mocked Services ---
# You can create a generic mock factory or specific ones like below

@pytest.fixture
def mock_prompt_service():
    return MagicMock(spec=PromptService)

@pytest.fixture
def mock_manga_room_service():
    return MagicMock(spec=MangaRoomService)

@pytest.fixture
def mock_creation_story_service():
    return MagicMock(spec=CreationStoryService)

@pytest.fixture
def mock_member_service():
    return MagicMock(spec=MemberService)

@pytest.fixture
def mock_notification_service():
    return MagicMock(spec=NotificationService)

@pytest.fixture
def mock_user_service():
    return MagicMock(spec=UserService)


# --- Dependency Overrides ---
# Example for PromptService. You'll need to do this for all services you want to mock.

@pytest.fixture(autouse=True) # autouse=True applies this to all tests
def override_dependencies(
    mock_prompt_service,
    mock_manga_room_service,
    mock_creation_story_service,
    mock_member_service,
    mock_notification_service,
    mock_user_service
):
    app.dependency_overrides[get_prompt_service] = lambda: mock_prompt_service
    app.dependency_overrides[get_manga_room_service] = lambda: mock_manga_room_service
    app.dependency_overrides[get_creation_story_service] = lambda: mock_creation_story_service
    app.dependency_overrides[get_member_service] = lambda: mock_member_service
    app.dependency_overrides[get_notification_service] = lambda: mock_notification_service
    app.dependency_overrides[get_user_service] = lambda: mock_user_service # Assuming

    yield

    # Clear overrides after tests
    app.dependency_overrides = {}
