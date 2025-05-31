from sqlalchemy.orm import Session
from app.models.member_model import Member
from app.schemas.member_schema import MemberCreate, MemberUpdate
from typing import Optional # Add this import

class MemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, member_create: MemberCreate) -> Member:
        db_member = Member(**member_create.model_dump())
        self.db.add(db_member)
        self.db.commit()
        self.db.refresh(db_member)
        return db_member

    def get_by_id(self, member_id: int) -> Member | None:
        return self.db.query(Member).filter(Member.id == member_id).first()

    def get_all(self, user_id: Optional[int] = None) -> list[Member]:
        query = self.db.query(Member)
        if user_id is not None:
            query = query.filter(Member.user_id == user_id)
        return query.all()

    def update(self, member_id: int, member_update: MemberUpdate) -> Member | None:
        db_member = self.get_by_id(member_id)
        if db_member:
            update_data = member_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_member, key, value)
            self.db.commit()
            self.db.refresh(db_member)
        return db_member

    def delete(self, member_id: int) -> Member | None:
        db_member = self.get_by_id(member_id)
        if db_member:
            self.db.delete(db_member)
            self.db.commit()
        return db_member
