from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreationStoryBase(BaseModel):
    title: str
    manga_room_id: int

class CreationStoryCreate(CreationStoryBase):
    pass

class CreationStoryUpdate(BaseModel):
    title: Optional[str] = None
    # manga_room_id is typically not updated, but can be added if needed.

class CreationStoryRead(CreationStoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
