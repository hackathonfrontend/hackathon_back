from sqlalchemy import Column, Integer, ForeignKey
from config.database import Base

class Member(Base):
    __tablename__ = "members"

    user_id = Column(Integer, primary_key=True, index=True)  # Make user_id the primary key
    manga_room_id = Column(Integer, nullable=False)
    # user = relationship("User", back_populates="memberships")
    # manga_room = relationship("MangaRoom", back_populates="members", foreign_keys=[manga_room_id])