# CashApp/backend/app/routers/health.py
from fastapi import APIRouter
import os

router = APIRouter(tags=["health"])

@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "cashapp-backend",
        "env": os.getenv("APP_ENV", "unknown"),
    }
