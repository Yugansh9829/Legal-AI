from fastapi import APIRouter
from app.api.v1.endpoints.health import health_router


api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["health"])