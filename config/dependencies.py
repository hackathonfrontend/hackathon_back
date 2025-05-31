from sqlalchemy.ext.declarative import declarative_base
from app.services.user_service import UserService
from fastapi import Depends
from app.repositories.user_repository import UserRepository
from config.database import get_db  # assumes you have a get_db dependency

def get_user_service(db=Depends(get_db)):
    return UserService(UserRepository(db))

user_service_dependency = get_user_service
Base = declarative_base()