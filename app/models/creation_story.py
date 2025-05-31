from sqlalchemy import Column, Integer, Text, ForeignKey
from config.base import Base

class CreationStory(Base):
    __tablename__ = "creation_stories"
    id = Column(Integer, primary_key=True, index=True)
    manga_id = Column(Integer, ForeignKey("manga_rooms.id"), nullable=False)
    user_text = Column(Text, nullable=False)
    gpt_text = Column(Text, nullable=False)