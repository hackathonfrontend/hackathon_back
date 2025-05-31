from pydantic import BaseModel
from typing import Optional

class MangaRoomBase(BaseModel):
    user_id: int
    userPrompt: str # Assuming Text from model maps to str
    pagesPerUser: int

class MangaRoomCreate(MangaRoomBase):
    pass

class MangaRoomUpdate(BaseModel): # Changed to BaseModel for explicit optional fields
    user_id: Optional[int] = None
    userPrompt: Optional[str] = None
    pagesPerUser: Optional[int] = None

class MangaRoomRead(MangaRoomBase):
    id: int
    room_id: int  # Changed to int

    class Config:
        orm_mode = True

class MangaRoomStringIdResponse(BaseModel):
    room_id: int  # Changed to int