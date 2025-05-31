from sqlalchemy import Column, Integer, String, ForeignKey
from config.base import Base

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, index=True)
    manga_id = Column(Integer, ForeignKey("manga_rooms.id"), nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_number = Column(Integer, nullable=False)
    panel = Column(String, nullable=True)  # URL to image in Firebase