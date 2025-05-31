from sqlalchemy.orm import Session
from app.models.prompt_model import Prompt
from app.schemas.prompt_schema import PromptCreate, PromptUpdate
from typing import Optional  # Add this import

class PromptRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, prompt_create: PromptCreate) -> Prompt:
        db_prompt = Prompt(**prompt_create.model_dump())
        self.db.add(db_prompt)
        self.db.commit()
        self.db.refresh(db_prompt)
        return db_prompt

    def get_by_id(self, prompt_id: int) -> Prompt | None:
        return self.db.query(Prompt).filter(Prompt.id == prompt_id).first()

    def get_all(self, user_id: Optional[int] = None) -> list[Prompt]:
        query = self.db.query(Prompt)
        if user_id is not None:
            query = query.filter(Prompt.user_id == user_id)
        return query.all()

    def update(self, prompt_id: int, prompt_update: PromptUpdate) -> Prompt | None:
        db_prompt = self.get_by_id(prompt_id)
        if db_prompt:
            update_data = prompt_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_prompt, key, value)
            self.db.commit()
            self.db.refresh(db_prompt)
        return db_prompt

    def delete(self, prompt_id: int) -> Prompt | None:
        db_prompt = self.get_by_id(prompt_id)
        if db_prompt:
            self.db.delete(db_prompt)
            self.db.commit()
        return db_prompt
