from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.schemas.manga_room_schema import MangaRoomCreate, MangaRoomRead, MangaRoomUpdate
from app.services.manga_room_service import MangaRoomService
from config.dependencies import get_db, get_manga_room_service # Assuming you use the alias

router = APIRouter(
    prefix="/manga-rooms",
    tags=["manga-rooms"]
)

@router.post("/", response_model=MangaRoomRead, status_code=status.HTTP_201_CREATED)
def create_manga_room(
    manga_room_create: MangaRoomCreate,
    manga_room_service: MangaRoomService = Depends(get_manga_room_service)
):
    return manga_room_service.create_manga_room(manga_room_create=manga_room_create)

@router.get("/{room_id}", response_model=MangaRoomRead)
def get_manga_room(
    room_id: int,
    manga_room_service: MangaRoomService = Depends(get_manga_room_service)
):
    db_manga_room = manga_room_service.get_manga_room_by_id(room_id=room_id)
    if db_manga_room is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MangaRoom not found")
    return db_manga_room

@router.get("/", response_model=list[MangaRoomRead])
def get_all_manga_rooms(
    user_id: Optional[int] = None, # Add user_id as an optional query parameter
    manga_room_service: MangaRoomService = Depends(get_manga_room_service) # Or Depends(get_manga_room_service)
):
    return manga_room_service.get_all_manga_rooms(user_id=user_id)

@router.put("/{room_id}", response_model=MangaRoomRead)
def update_manga_room(
    room_id: int,
    manga_room_update: MangaRoomUpdate,
    manga_room_service: MangaRoomService = Depends(get_manga_room_service)
):
    updated_manga_room = manga_room_service.update_manga_room(room_id=room_id, manga_room_update=manga_room_update)
    if updated_manga_room is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MangaRoom not found")
    return updated_manga_room

@router.delete("/{room_id}", response_model=MangaRoomRead)
def delete_manga_room(
    room_id: int,
    manga_room_service: MangaRoomService = Depends(get_manga_room_service)
):
    deleted_manga_room = manga_room_service.delete_manga_room(room_id=room_id)
    if deleted_manga_room is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MangaRoom not found")
    return deleted_manga_room