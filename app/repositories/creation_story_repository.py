from sqlalchemy.orm import Session
from app.models.creation_story_model import CreationStory
from app.schemas.creation_story_schema import CreationStoryCreate, CreationStoryUpdate
from typing import Optional # Add this import

class CreationStoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, creation_story_create: CreationStoryCreate) -> CreationStory:
        db_creation_story = CreationStory(**creation_story_create.model_dump())
        self.db.add(db_creation_story)
        self.db.commit()
        self.db.refresh(db_creation_story)
        return db_creation_story

    def get_by_id(self, story_id: int) -> CreationStory | None:
        return self.db.query(CreationStory).filter(CreationStory.id == story_id).first()

    def get_all(self, manga_room_id: Optional[int] = None) -> list[CreationStory]:
        query = self.db.query(CreationStory)
        if manga_room_id is not None:
            # Assuming your CreationStory model has a 'manga_room_id' field
            query = query.filter(CreationStory.manga_room_id == manga_room_id)
        return query.all()

    def update(self, story_id: int, creation_story_update: CreationStoryUpdate) -> CreationStory | None:
        db_creation_story = self.get_by_id(story_id)
        if db_creation_story:
            update_data = creation_story_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_creation_story, key, value)
            self.db.commit()
            self.db.refresh(db_creation_story)
        return db_creation_story

    def delete(self, story_id: int) -> CreationStory | None:
        db_creation_story = self.get_by_id(story_id)
        if db_creation_story:
            self.db.delete(db_creation_story)
            self.db.commit()
        return db_creation_story
