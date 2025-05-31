from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal # Assuming SessionLocal is your session factory

# Import Services
from app.services.prompt_service import PromptService
from app.services.creation_story_service import CreationStoryService
from app.services.member_service import MemberService
from app.services.notification_service import NotificationService
from app.services.user_service import UserService
from app.services.manga_room_service import MangaRoomService

# Import Repositories
from app.repositories.user_repository import UserRepository # Assuming this exists
from app.repositories.manga_room_repository import MangaRoomRepository
from app.repositories.prompt_repository import PromptRepository
from app.repositories.creation_story_repository import CreationStoryRepository
from app.repositories.member_repository import MemberRepository
from app.repositories.notification_repository import NotificationRepository


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_service(db: Session =Depends(get_db)):
    return UserService(UserRepository(db))

def get_manga_room_service(db: Session = Depends(get_db)) -> MangaRoomService:
    return MangaRoomService(MangaRoomRepository(db))

def get_prompt_service(db: Session = Depends(get_db)) -> PromptService:
    return PromptService(PromptRepository(db))

def get_creation_story_service(db: Session = Depends(get_db)) -> CreationStoryService:
    return CreationStoryService(CreationStoryRepository(db))

def get_member_service(db: Session = Depends(get_db)) -> MemberService:
    return MemberService(MemberRepository(db))

def get_notification_service(db: Session = Depends(get_db)) -> NotificationService:
    return NotificationService(NotificationRepository(db))

user_service_dependency = get_user_service
manga_room_service_dependency = get_manga_room_service
prompt_service_dependency = get_prompt_service
creation_story_service_dependency = get_creation_story_service
member_service_dependency = get_member_service
notification_service_dependency = get_notification_service