# user_model.py
from sqlalchemy import Column, Integer, String
from config.base import Base
from sqlalchemy.orm import relationship
from .manga_room import MangaRoom

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    manga_rooms = relationship(
        "MangaRoom",
        backref="user",
        cascade="all, delete",
        passive_deletes=True
    )