from sqlalchemy import Column, Integer, Text, ForeignKey
from config.base import Base

class MangaRoom(Base):
    __tablename__ = "manga_rooms"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    userPrompt = Column(Text, nullable=False)
    pagesPerUser = Column(Integer, nullable=False)