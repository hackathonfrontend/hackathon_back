from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base # Assuming Base is defined in config.database

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True, nullable=False)
    creation_story_id = Column(Integer, ForeignKey("creation_stories.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Assuming a 'users' table

    # Example relationships (adjust as needed)
    # creation_story = relationship("CreationStory", back_populates="prompts")
    # user = relationship("User", back_populates="prompts")