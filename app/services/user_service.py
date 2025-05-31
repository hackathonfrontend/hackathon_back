from sqlalchemy.orm import Session
from app.models.user_model import User # Changed back if it was app.models.user
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all()

    def create_user(self, username: str, password: str):
        return self.user_repository.create(username, password)