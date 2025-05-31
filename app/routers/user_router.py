
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate
from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserRead, UserLogin
from config.dependencies import user_service_dependency  # define this dependency to provide UserService
from app.services.auth_service import hash_password, verify_password, create_access_token
from app.models.user_model import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
def get_users(user_service: UserService = Depends(user_service_dependency)):
    return user_service.get_all_users()

@router.post("/", response_model=UserRead)
def create_user(user_create: UserCreate, user_service: UserService = Depends(user_service_dependency)):
    return user_service.create_user(
        username=user_create.username,
        password=user_create.password
    )

@router.post("/register", response_model=UserRead)
def register(user_create: UserCreate, user_service: UserService = Depends(user_service_dependency)):
    user = user_service.get_by_username(user_create.username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = hash_password(user_create.password)
    return user_service.create_user(username=user_create.username, password=hashed_pw)

@router.post("/login")
def login(user_login: UserLogin, user_service: UserService = Depends(user_service_dependency)):
    user = user_service.get_by_username(user_login.username)
    if not user or not verify_password(user_login.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username, "user_id": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id
    }

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, user_service: UserService = Depends(user_service_dependency)):
    user = user_service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_service.delete_user(user_id)