from fastapi import APIRouter, Request

from app.db.mongo_client import MongoORM
from app.schemas import RoomSuccessResponse
from app.schemas.failure_response import FailureResponse

room_router = APIRouter(prefix="/rooms")


@room_router.get(
    "/", response_model=RoomSuccessResponse, responses={404: {"model": FailureResponse}}
)
async def get_rooms(request: Request) -> RoomSuccessResponse:
    db: MongoORM = request.app.state.db
    rooms = await db.get_all_rooms()
    room_names = [room.room for room in rooms]
    return RoomSuccessResponse(data=room_names)
