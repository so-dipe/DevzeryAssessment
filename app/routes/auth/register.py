from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ...db.db import engine, get_db
from ...db.models import Base
from ...db.crud import create_user, get_user_by_verification_token
from .pydantic_models import CreateUserRequest
from .verification_utils import generate_verification_token, send_verification_email

router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.post("/register")
async def create_account(request: CreateUserRequest, db: Session = Depends(get_db)):
    token = generate_verification_token()
    try:
        await send_verification_email(request.email, token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to send verification email: {str(e)}")
    
    try:
        create_user(db, request.username, request.email, request.password, verification_token=token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create user: {str(e)}")

    return JSONResponse(content={"message": "User registered successfully. Verification email sent."})

@router.get("/verify")
def vefify_email(token: str, db: Session = Depends(get_db)):
    user = get_user_by_verification_token(db, token)
    if not user:
        raise HTTPException(status_code=404, detail="Token not found")

    user.is_email_verified = True
    user.verification_token = None
    db.commit()

    return JSONResponse(content={"message": "Email verified successfully."})
