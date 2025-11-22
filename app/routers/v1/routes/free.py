from fastapi import APIRouter, Depends, Request
from typing import Annotated

from app.db.mongo_client import MongoORM
from app.schemas.params import FreeRoomParams
from app.schemas import FreeRoomSuccessResponse
from app.schemas.failure_response import FailureResponse

free_router = APIRouter(prefix="/free")


@free_router.get(
    "/",
    response_model=FreeRoomSuccessResponse,
)
async def get_free_rooms(
    request: Request,
    params: Annotated[FreeRoomParams, Depends()],
) -> FreeRoomSuccessResponse:
    db: MongoORM = request.app.state.db
    free_rooms = await db.get_room_availabilities(**params.model_dump())

    return FreeRoomSuccessResponse(data=free_rooms)
