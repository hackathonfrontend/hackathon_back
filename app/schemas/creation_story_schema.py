from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreationStoryBase(BaseModel):
    title: str
    manga_id: int # Changed from str to int
    user_text: str # Assuming Text maps to str
    gpt_text: str # Assuming Text maps to str


class CreationStoryCreate(CreationStoryBase):
    pass

class CreationStoryUpdate(BaseModel):
    title: Optional[str] = None
    user_text: Optional[str] = None
    gpt_text: Optional[str] = None
    # manga_id is typically not updated for an existing story, but can be added if needed.

class CreationStoryRead(CreationStoryBase):
    id: int # Assuming CreationStory.id remains int
    # created_at: datetime # Add if these fields exist in your model and you want them in read schema
    # updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
