from sqlalchemy import Column, Integer, ForeignKey
from config.base import Base

class Member(Base):
    __tablename__ = "members"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    manga_room_id = Column(Integer, ForeignKey("manga_rooms.id"), primary_key=True)