from sqlalchemy.orm import Session
from app.models.user_model import User

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

    def get_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username == username).first()
    def delete(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()