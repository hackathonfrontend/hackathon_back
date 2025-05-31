from pydantic import BaseModel
from typing import Optional

class PromptBase(BaseModel):
    text: str
    creation_story_id: int
    user_id: int # Assuming a user creates the prompt

class PromptCreate(PromptBase):
    pass

class PromptUpdate(BaseModel):
    text: Optional[str] = None
    # creation_story_id and user_id are typically not updated,
    # but can be added if needed.

class PromptRead(PromptBase):
    id: int


    class Config:
        orm_mode = True
