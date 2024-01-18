from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True, unique=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    verification_token = Column(String(255), nullable=True) 
    is_email_verified = Column(Boolean, default=False)
