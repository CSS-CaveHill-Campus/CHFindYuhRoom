from fastapi import APIRouter, Depends
from typing import Annotated

from app.db.dependencies import get_db
from app.db.mongo_client import MongoORM
from app.schemas import RoomSuccessResponse

room_router = APIRouter(prefix="/rooms")


@room_router.get("/", response_model=RoomSuccessResponse)
async def get_rooms(db: Annotated[MongoORM, Depends(get_db)]) -> RoomSuccessResponse:
    rooms = await db.get_all_rooms()
    room_names = [room.room for room in rooms]
    return RoomSuccessResponse(data=room_names)
