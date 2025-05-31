from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.schemas.creation_story_schema import CreationStoryCreate, CreationStoryRead, CreationStoryUpdate
from app.services.creation_story_service import CreationStoryService
from config.dependencies import get_db, get_creation_story_service

router = APIRouter(
    prefix="/creation-stories",
    tags=["creation-stories"]
)

@router.post("/", response_model=CreationStoryRead, status_code=status.HTTP_201_CREATED)
def create_creation_story(
    creation_story_create: CreationStoryCreate,
    creation_story_service: CreationStoryService = Depends(get_creation_story_service)
):
    return creation_story_service.create_creation_story(creation_story_create=creation_story_create)

@router.get("/{story_id}", response_model=CreationStoryRead)
def get_creation_story(
    story_id: int,
    creation_story_service: CreationStoryService = Depends(get_creation_story_service)
):
    db_creation_story = creation_story_service.get_creation_story_by_id(story_id=story_id)
    if db_creation_story is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CreationStory not found")
    return db_creation_story

@router.get("/", response_model=list[CreationStoryRead])
def get_all_creation_stories(
    manga_room_id: Optional[int] = None,
    creation_story_service: CreationStoryService = Depends(get_creation_story_service)
):
    return creation_story_service.get_all_creation_stories(manga_room_id=manga_room_id)

@router.put("/{story_id}", response_model=CreationStoryRead)
def update_creation_story(
    story_id: int,
    creation_story_update: CreationStoryUpdate,
    creation_story_service: CreationStoryService = Depends(get_creation_story_service)
):
    updated_creation_story = creation_story_service.update_creation_story(story_id=story_id, creation_story_update=creation_story_update)
    if updated_creation_story is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CreationStory not found")
    return updated_creation_story

@router.delete("/{story_id}", response_model=CreationStoryRead)
def delete_creation_story(
    story_id: int,
    creation_story_service: CreationStoryService = Depends(get_creation_story_service)
):
    deleted_creation_story = creation_story_service.delete_creation_story(story_id=story_id)
    if deleted_creation_story is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="CreationStory not found")
    return deleted_creation_story
