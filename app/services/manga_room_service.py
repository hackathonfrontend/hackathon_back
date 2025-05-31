from sqlalchemy.orm import Session
from app.models.manga_room_model import MangaRoom
from app.schemas.manga_room_schema import MangaRoomCreate, MangaRoomUpdate
from app.repositories.manga_room_repository import MangaRoomRepository
from typing import Optional

class MangaRoomService:
    def __init__(self, manga_room_repository: MangaRoomRepository):
        self.manga_room_repository = manga_room_repository

    def create_manga_room(self, manga_room_create: MangaRoomCreate) -> MangaRoom:
        return self.manga_room_repository.create(manga_room_create=manga_room_create)

    def get_manga_room_by_room_id(self, room_id: int) -> MangaRoom | None: # Renamed and changed param type
        return self.manga_room_repository.get_by_room_id(room_id=room_id)

    def get_all_manga_rooms(self, user_id: Optional[int] = None) -> list[MangaRoom]:
        return self.manga_room_repository.get_all(user_id=user_id)

    def update_manga_room_by_room_id(self, room_id: int, manga_room_update: MangaRoomUpdate) -> MangaRoom | None: # Renamed and changed param type
        return self.manga_room_repository.update_by_room_id(room_id=room_id, manga_room_update=manga_room_update)

    def delete_manga_room_by_room_id(self, room_id: int) -> MangaRoom | None: # Renamed and changed param type
        return self.manga_room_repository.delete_by_room_id(room_id=room_id)