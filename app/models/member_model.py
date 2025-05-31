from sqlalchemy import Column, Integer, ForeignKey
from config.database import Base

class Member(Base):
    __tablename__ = "members"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True, nullable=False)
    manga_room_id = Column(Integer, ForeignKey("manga_rooms.id"), primary_key=True, nullable=False) # Changed FK to manga_rooms.id
    # user = relationship("User", back_poulates="memberships")
    # manga_room = relationship("MangaRopom", back_populates="members", foreign_keys=[manga_room_id])