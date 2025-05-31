from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.schemas.member_schema import MemberCreate, MemberRead, MemberUpdate
from app.services.member_service import MemberService
from app.services.manga_room_service import MangaRoomService # Add this import
from app.services.user_service import UserService # Assuming you have a UserService for user operations
from config.dependencies import get_member_service, get_manga_room_service # Add get_manga_room_service

router = APIRouter(
    prefix="/members",
    tags=["members"]
)

@router.post("/", response_model=MemberRead, status_code=status.HTTP_201_CREATED)
def create_member(
    member_create: MemberCreate,
    member_service: MemberService = Depends(get_member_service),
    manga_room_service: MangaRoomService = Depends(get_manga_room_service)
):
    # Check if the manga_room exists by its primary id
    db_manga_room = manga_room_service.get_manga_room_by_id(id=member_create.manga_room_id)
    if db_manga_room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"MangaRoom with id '{member_create.manga_room_id}' not found. Cannot create member."
        )
    return member_service.create_member(member_create=member_create)

@router.post("/manga-room/{manga_room_id}/user/{user_id}", response_model=MemberRead, status_code=status.HTTP_201_CREATED)
def create_member_for_manga_room_and_user(
    manga_room_id: int,
    user_id: int,
    member_service: MemberService = Depends(get_member_service),
    manga_room_service: MangaRoomService = Depends(get_manga_room_service),
    user_service: UserService = Depends(get_manga_room_service) # Assuming user_service_dependency is defined in config.dependencies
):
    # Check if the user exists
    db_user = user_service.get_by_id(user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{user_id}' not found. Cannot create member."
        )

    # Check if the manga_room exists by its primary id
    db_manga_room = manga_room_service.get_manga_room_by_id(id=manga_room_id)
    if db_manga_room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"MangaRoom with id '{manga_room_id}' not found. Cannot create member."
        )

    # Create MemberCreate schema instance
    member_create_data = MemberCreate(user_id=user_id, manga_room_id=manga_room_id)
    
    # Attempt to create the member
    # This might still fail if the (user_id, manga_room_id) combination already exists due to the composite primary key
    try:
        created_member = member_service.create_member(member_create=member_create_data)
    except Exception as e: # Catch generic exception, ideally a more specific one for duplicate entry
        # You might want to check for specific database errors indicating a duplicate primary key
        # For psycopg2, this could be psycopg2.errors.UniqueViolation
        # For SQLAlchemy, it might be sqlalchemy.exc.IntegrityError
        # This is a basic catch-all for now.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, # 409 Conflict is appropriate for duplicate resource
            detail=f"Member with user_id '{user_id}' and manga_room_id '{manga_room_id}' may already exist or another integrity error occurred."
        )
    return created_member

@router.get("/{member_id}", response_model=MemberRead)
def get_member(
    member_id: int,
    member_service: MemberService = Depends(get_member_service)
):
    db_member = member_service.get_member_by_id(member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")
    return db_member

@router.get("/", response_model=list[MemberRead])
def get_all_members(
    user_id: Optional[int] = None,
    member_service: MemberService = Depends(get_member_service)
):
    return member_service.get_all_members(user_id=user_id)

@router.put("/{member_id}", response_model=MemberRead)
def update_member(
    member_id: int,
    member_update: MemberUpdate,
    member_service: MemberService = Depends(get_member_service)
):
    updated_member = member_service.update_member(member_id=member_id, member_update=member_update)
    if updated_member is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")
    return updated_member

@router.delete("/{member_id}", response_model=MemberRead)
def delete_member(
    member_id: int,
    member_service: MemberService = Depends(get_member_service)
):
    deleted_member = member_service.delete_member(member_id=member_id)
    if deleted_member is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Member not found")
    return deleted_member
