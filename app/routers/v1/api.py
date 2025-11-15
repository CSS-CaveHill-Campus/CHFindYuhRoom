from fastapi import APIRouter
from app.routers.v1.routes import free_router, room_router, prefixes_router, schedule_router

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(free_router)
v1_router.include_router(room_router)
v1_router.include_router(prefixes_router)
v1_router.include_router(schedule_router)
