from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NotificationBase(BaseModel):
    user_id: int
    message: str

class NotificationCreate(NotificationBase):
    pass

class NotificationUpdate(BaseModel):
    message: Optional[str] = None
    is_read: Optional[bool] = None

class NotificationRead(NotificationBase):
    id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
