from sqlalchemy.orm import Session
from app.models.user_model import User  # Changed back if it was app.models.user

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(User).all()

    def create(self, username: str, password: str):
        user = User(username=username, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user