from fastapi import APIRouter, Depends
from typing import Annotated

from app.db.dependencies import get_db
from app.db.mongo_client import MongoORM
from app.schemas.params import FreeRoomParams
from app.schemas import FreeRoomSuccessResponse

free_router = APIRouter(prefix="/free")


@free_router.get(
    "/",
    response_model=FreeRoomSuccessResponse,
)
async def get_free_rooms(
    db: Annotated[MongoORM, Depends(get_db)],
    params: Annotated[FreeRoomParams, Depends()],
) -> FreeRoomSuccessResponse:
    free_rooms = await db.get_room_availabilities(
        day=params.day,
        hour=params.hour,
        duration=params.duration,
        room=params.room,
    )
    return FreeRoomSuccessResponse(data=free_rooms)
