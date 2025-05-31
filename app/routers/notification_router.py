from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional # Ensure this is imported
from app.schemas.notification_schema import NotificationCreate, NotificationRead, NotificationUpdate
from app.services.notification_service import NotificationService
from config.dependencies import get_notification_service # Or your aliased dependency

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

@router.post("/", response_model=NotificationRead, status_code=status.HTTP_201_CREATED)
def create_notification(
    notification_create: NotificationCreate,
    notification_service: NotificationService = Depends(get_notification_service)
):
    return notification_service.create_notification(notification_create=notification_create)

@router.get("/{notification_id}", response_model=NotificationRead)
def get_notification(
    notification_id: int,
    notification_service: NotificationService = Depends(get_notification_service)
):
    db_notification = notification_service.get_notification_by_id(notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    return db_notification

@router.get("/", response_model=list[NotificationRead])
def get_all_notifications(
    user_id: Optional[int] = None, # user_id is already here
    notification_service: NotificationService = Depends(get_notification_service)
):
    return notification_service.get_all_notifications(user_id=user_id)

@router.put("/{notification_id}", response_model=NotificationRead)
def update_notification(
    notification_id: int,
    notification_update: NotificationUpdate,
    notification_service: NotificationService = Depends(get_notification_service)
):
    updated_notification = notification_service.update_notification(notification_id=notification_id, notification_update=notification_update)
    if updated_notification is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    return updated_notification

@router.delete("/{notification_id}", response_model=NotificationRead)
def delete_notification(
    notification_id: int,
    notification_service: NotificationService = Depends(get_notification_service)
):
    deleted_notification = notification_service.delete_notification(notification_id=notification_id)
    if deleted_notification is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    return deleted_notification
