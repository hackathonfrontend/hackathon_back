from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.schemas.prompt_schema import PromptCreate, PromptRead, PromptUpdate
from app.services.prompt_service import PromptService
from config.dependencies import get_db, get_prompt_service

router = APIRouter(
    prefix="/prompts",
    tags=["prompts"]
)

@router.post("/", response_model=PromptRead, status_code=status.HTTP_201_CREATED)
def create_prompt(
    prompt_create: PromptCreate,
    prompt_service: PromptService = Depends(get_prompt_service)
):
    return prompt_service.create_prompt(prompt_create=prompt_create)

@router.get("/{prompt_id}", response_model=PromptRead)
def get_prompt(
    prompt_id: int,
    prompt_service: PromptService = Depends(get_prompt_service)
):
    db_prompt = prompt_service.get_prompt_by_id(prompt_id=prompt_id)
    if db_prompt is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found")
    return db_prompt

@router.get("/", response_model=list[PromptRead])
def get_all_prompts(
    user_id: Optional[int] = None,
    prompt_service: PromptService = Depends(get_prompt_service)
):
    return prompt_service.get_all_prompts(user_id=user_id)

@router.put("/{prompt_id}", response_model=PromptRead)
def update_prompt(
    prompt_id: int,
    prompt_update: PromptUpdate,
    prompt_service: PromptService = Depends(get_prompt_service)
):
    updated_prompt = prompt_service.update_prompt(prompt_id=prompt_id, prompt_update=prompt_update)
    if updated_prompt is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found")
    return updated_prompt

@router.delete("/{prompt_id}", response_model=PromptRead)
def delete_prompt(
    prompt_id: int,
    prompt_service: PromptService = Depends(get_prompt_service)
):
    deleted_prompt = prompt_service.delete_prompt(prompt_id=prompt_id)
    if deleted_prompt is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found")
    return deleted_prompt
