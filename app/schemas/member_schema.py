from pydantic import BaseModel
from typing import Optional

class MemberBase(BaseModel):
    user_id: int
    manga_room_id: int
    role: Optional[str] = "member"

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    role: Optional[str] = None
    # user_id and manga_room_id are typically not updated for a membership record.
    # If they need to be, they can be added here.

class MemberRead(MemberBase):
    id: int

    class Config:
        orm_mode = True
