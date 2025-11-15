from fastapi import APIRouter

from app.schemas import RoomSuccessResponse
from app.schemas.failure_response import FailureResponse

room_router = APIRouter(prefix="/rooms")


@room_router.get("/", response_model=RoomSuccessResponse, responses={404: {"model": FailureResponse}})
async def get_rooms() -> RoomSuccessResponse:
    pass  # DB call
