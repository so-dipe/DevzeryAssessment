from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    email: str
    is_email_verified: bool

class UpdateUserModel(BaseModel):
    username: str = None
    email: str = None