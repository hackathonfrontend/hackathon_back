from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate
from fastapi import APIRouter, Depends
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserRead
from config.dependencies import get_user_service  # define this dependency to provide UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
def get_all_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()

@router.post("/", response_model=UserRead)
def create_user(user_create: UserCreate, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(
        username=user_create.username,
        password=user_create.password
    )