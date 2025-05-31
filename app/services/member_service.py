from sqlalchemy.orm import Session
from app.models.member_model import Member
from app.schemas.member_schema import MemberCreate, MemberUpdate
from app.repositories.member_repository import MemberRepository
from typing import Optional # Add this import

class MemberService:
    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

    def create_member(self, member_create: MemberCreate) -> Member:
        return self.member_repository.create(member_create=member_create)

    def get_member_by_id(self, member_id: int) -> Member | None:
        return self.member_repository.get_by_id(member_id=member_id)

    def get_all_members(self, user_id: Optional[int] = None) -> list[Member]:
        return self.member_repository.get_all(user_id=user_id)

    def update_member(self, member_id: int, member_update: MemberUpdate) -> Member | None:
        return self.member_repository.update(member_id=member_id, member_update=member_update)

    def delete_member(self, member_id: int) -> Member | None:
        return self.member_repository.delete(member_id=member_id)
