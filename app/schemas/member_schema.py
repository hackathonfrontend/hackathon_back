from pydantic import BaseModel
from typing import Optional

class MemberBase(BaseModel):
    user_id: int
    manga_room_id: int # Changed from str to int

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    pass


class MemberRead(MemberBase):
    id: int

    class Config:
        orm_mode = True
