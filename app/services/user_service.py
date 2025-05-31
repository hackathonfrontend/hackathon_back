from sqlalchemy.orm import Session
from app.models.user_model import User # Changed back if it was app.models.user
from app.repositories.user_repository import UserRepository

from app.models.user_model import User
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all()

    def create_user(self, username: str, password: str):
        return self.user_repository.create(username, password)

    def get_by_username(self, username: str) -> User | None:
        return self.user_repository.get_by_username(username)
    def delete_user(self, user_id: int):
        self.user_repository.delete(user_id)

    def get_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_by_id(user_id)