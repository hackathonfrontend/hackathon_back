from sqlalchemy.orm import Session
from app.models.manga_room_model import MangaRoom
from app.schemas.manga_room_schema import MangaRoomCreate, MangaRoomUpdate
from typing import Optional

class MangaRoomRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, manga_room_create: MangaRoomCreate) -> MangaRoom:
        db_manga_room = MangaRoom(**manga_room_create.model_dump())
        self.db.add(db_manga_room)
        self.db.commit()
        self.db.refresh(db_manga_room)
        return db_manga_room

    def get_by_primary_id(self, id: int) -> MangaRoom | None: # New method to get by primary key 'id'
        return self.db.query(MangaRoom).filter(MangaRoom.id == id).first()

    def get_by_room_id(self, room_id: int) -> MangaRoom | None: # Renamed and changed param type
        return self.db.query(MangaRoom).filter(MangaRoom.room_id == room_id).first()

    def get_all(self, user_id: Optional[int] = None) -> list[MangaRoom]:
        query = self.db.query(MangaRoom)
        if user_id is not None:
            query = query.filter(MangaRoom.user_id == user_id)
        return query.all()

    def update_by_room_id(self, room_id: int, manga_room_update: MangaRoomUpdate) -> MangaRoom | None: # Renamed and changed param type
        db_manga_room = self.get_by_room_id(room_id=room_id)
        if db_manga_room:
            update_data = manga_room_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_manga_room, key, value)
            self.db.commit()
            self.db.refresh(db_manga_room)
        return db_manga_room

    def delete_by_room_id(self, room_id: int) -> MangaRoom | None: # Renamed and changed param type
        db_manga_room = self.get_by_room_id(room_id=room_id)
        if db_manga_room:
            self.db.delete(db_manga_room)
            self.db.commit()
        return db_manga_room
