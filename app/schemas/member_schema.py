from pydantic import BaseModel
from typing import Optional

class MemberBase(BaseModel):
    user_id: int
    manga_room_id: int # This should refer to manga_rooms.id

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    pass


class MemberRead(MemberBase): # user_id and manga_room_id are inherited from MemberBase
    # No separate 'id' field if the primary key is composite (user_id, manga_room_id)
    class Config:
        orm_mode = True
