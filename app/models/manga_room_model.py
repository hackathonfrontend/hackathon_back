from sqlalchemy import Column, Integer, Text, ForeignKey
from config.database import Base # Assuming Base is defined in config.database
from app.utils.id_generator import generate_manga_room_id # Import the generator

class MangaRoom(Base):
    __tablename__ = "manga_rooms"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) # Reverted to Integer, autoincrementing
    room_id = Column(Integer, default=generate_manga_room_id, unique=True, index=True, nullable=False) # Changed to Integer
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    userPrompt = Column(Text, nullable=False)
    pagesPerUser = Column(Integer, nullable=False)

    # Add relationships if they exist, e.g.,
    # creation_stories = relationship("CreationStory", back_populates="manga_room", foreign_keys="[CreationStory.manga_id]")
    # members = relationship("Member", back_populates="manga_room", foreign_keys="[Member.manga_room_id]")