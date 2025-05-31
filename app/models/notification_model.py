from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime,Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base # Assuming Base is defined in config.database

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # User to whom notification is sent
    text = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Example relationship (adjust as needed)
    # user = relationship("User", back_populates="notifications")
