from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .models import User
from passlib.hash import bcrypt

def create_user(db: Session, username: str, email: str, password: str, verification_token: str = None):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    # Create the new user
    hashed_password = bcrypt.hash(password)
    db_user = User(username=username, email=email, password=hashed_password, verification_token=verification_token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_verification_token(db: Session, verification_token: str):
    return db.query(User).filter(User.verification_token == verification_token).first()

def update_user(db: Session, user_id: int, username: str = None, email: str = None):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if username:
            db_user.username = username
        if email:
            db_user.email = email
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


