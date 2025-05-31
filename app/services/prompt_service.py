from sqlalchemy.orm import Session
from app.models.prompt_model import Prompt  # Changed back
from app.schemas.prompt_schema import PromptCreate, PromptUpdate
from app.repositories.prompt_repository import PromptRepository
from typing import Optional # Add this import

class PromptService:
    def __init__(self, prompt_repository: PromptRepository):
        self.prompt_repository = prompt_repository

    def create_prompt(self, prompt_create: PromptCreate) -> Prompt:
        return self.prompt_repository.create(prompt_create=prompt_create)

    def get_prompt_by_id(self, prompt_id: int) -> Prompt | None:
        return self.prompt_repository.get_by_id(prompt_id=prompt_id)

    def get_all_prompts(self, user_id: Optional[int] = None) -> list[Prompt]:
        return self.prompt_repository.get_all(user_id=user_id)

    def update_prompt(self, prompt_id: int, prompt_update: PromptUpdate) -> Prompt | None:
        return self.prompt_repository.update(prompt_id=prompt_id, prompt_update=prompt_update)

    def delete_prompt(self, prompt_id: int) -> Prompt | None:
        return self.prompt_repository.delete(prompt_id=prompt_id)
