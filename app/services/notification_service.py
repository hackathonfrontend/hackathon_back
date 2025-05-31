from sqlalchemy.orm import Session
from app.models.notification_model import Notification
from app.schemas.notification_schema import NotificationCreate, NotificationUpdate
from app.repositories.notification_repository import NotificationRepository
from typing import Optional # Ensure this is imported

class NotificationService:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    def create_notification(self, notification_create: NotificationCreate) -> Notification:
        return self.notification_repository.create(notification_create=notification_create)

    def get_notification_by_id(self, notification_id: int) -> Notification | None:
        return self.notification_repository.get_by_id(notification_id=notification_id)

    def get_all_notifications(self, user_id: Optional[int] = None) -> list[Notification]: # Removed skip and limit
        return self.notification_repository.get_all(user_id=user_id) # Removed skip and limit

    def update_notification(self, notification_id: int, notification_update: NotificationUpdate) -> Notification | None:
        return self.notification_repository.update(notification_id=notification_id, notification_update=notification_update)

    def delete_notification(self, notification_id: int) -> Notification | None:
        return self.notification_repository.delete(notification_id=notification_id)
