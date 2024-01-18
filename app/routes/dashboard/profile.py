from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .pydantic_models import UserModel, UpdateUserModel
from ..auth.access_token_utils import get_current_user
from ...db.db import get_db
from ...db.crud import get_all_users, update_user

router = APIRouter()

@router.get("/users/me", response_model=UserModel)
async def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user

@router.get("/users/", response_model=List[UserModel])
async def read_users(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    users = get_all_users(db=db)
    return users

@router.put("/users/me", response_model=UpdateUserModel)
async def update_user_details(
    db: Session = Depends(get_db),
    updated_user: UpdateUserModel = None, 
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # Update user details in the database
    if updated_user:
        updated_username = updated_user.username
        updated_email = updated_user.email
        updated_user_data = update_user(db, current_user.id, updated_username, updated_email)
    
        return updated_user_data
    else:
        {"message": "No data provided"}