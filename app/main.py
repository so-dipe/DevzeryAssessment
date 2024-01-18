from fastapi import FastAPI
from app.routes.auth.register import router as register_router
from app.routes.auth.login import router as login_router
from app.routes.dashboard.profile import router as profile_router
from config.config import Config

BASE_API = Config.BASE_API

app = FastAPI()

app.include_router(register_router, prefix=f"{BASE_API}/auth", tags=['Authentication'])
app.include_router(login_router, prefix=f"{BASE_API}/auth", tags=['Authentication'])
app.include_router(profile_router, prefix=f"{BASE_API}/dashboard", tags=['Dashboard'])