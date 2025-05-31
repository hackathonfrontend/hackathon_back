from sqlalchemy.orm import Session
from app.models.notification_model import Notification
from app.schemas.notification_schema import NotificationCreate, NotificationUpdate
from typing import Optional # Ensure this is imported

class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, notification_create: NotificationCreate) -> Notification:
        db_notification = Notification(**notification_create.model_dump())
        self.db.add(db_notification)
        self.db.commit()
        self.db.refresh(db_notification)
        return db_notification

    def get_by_id(self, notification_id: int) -> Notification | None:
        return self.db.query(Notification).filter(Notification.id == notification_id).first()

    def get_all(self, user_id: Optional[int] = None) -> list[Notification]: # Removed skip and limit
        query = self.db.query(Notification)
        if user_id is not None:
            query = query.filter(Notification.user_id == user_id)
        return query.all() # Removed .offset(skip).limit(limit)

    def update(self, notification_id: int, notification_update: NotificationUpdate) -> Notification | None:
        db_notification = self.get_by_id(notification_id)
        if db_notification:
            update_data = notification_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_notification, key, value)
            self.db.commit()
            self.db.refresh(db_notification)
        return db_notification

    def delete(self, notification_id: int) -> Notification | None:
        db_notification = self.get_by_id(notification_id)
        if db_notification:
            self.db.delete(db_notification)
            self.db.commit()
        return db_notification
