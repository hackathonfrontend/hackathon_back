from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.schemas.member_schema import MemberCreate, MemberRead, MemberUpdate
from app.services.member_service import MemberService
from config.dependencies import get_db, get_member_service

router = APIRouter(
    prefix="/members",
    tags=["members"]
)

@router.post("/", response_model=MemberRead, status_code=status.HTTP_201_CREATED)
def create_member(
    member_create: MemberCreate,
    member_service: MemberService = Depends(get_member_service)
):
    return member_service.create_member(member_create=member_create)

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
