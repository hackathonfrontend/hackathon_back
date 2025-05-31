from sqlalchemy.orm import Session
from app.models.creation_story_model import CreationStory
from app.schemas.creation_story_schema import CreationStoryCreate, CreationStoryUpdate
from app.repositories.creation_story_repository import CreationStoryRepository
from typing import Optional # Add this import

class CreationStoryService:
    def __init__(self, creation_story_repository: CreationStoryRepository):
        self.creation_story_repository = creation_story_repository

    def create_creation_story(self, creation_story_create: CreationStoryCreate) -> CreationStory:
        return self.creation_story_repository.create(creation_story_create=creation_story_create)

    def get_creation_story_by_id(self, story_id: int) -> CreationStory | None:
        return self.creation_story_repository.get_by_id(story_id=story_id)

    def get_all_creation_stories(self, manga_room_id: Optional[int] = None) -> list[CreationStory]:
        return self.creation_story_repository.get_all(manga_room_id=manga_room_id)

    def update_creation_story(self, story_id: int, creation_story_update: CreationStoryUpdate) -> CreationStory | None:
        return self.creation_story_repository.update(story_id=story_id, creation_story_update=creation_story_update)

    def delete_creation_story(self, story_id: int) -> CreationStory | None:
        return self.creation_story_repository.delete(story_id=story_id)
