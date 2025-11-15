from fastapi import APIRouter, Depends
from typing import Annotated

from app.schemas.params import FreeRoomParams
from app.schemas import FreeRoomSuccessResponse
from app.schemas.failure_response import FailureResponse

free_router = APIRouter(prefix="/free")


@free_router.get("/", response_model=FreeRoomSuccessResponse, responses={404: {"model": FailureResponse}})
async def get_free_rooms(
    params: Annotated[FreeRoomParams, Depends()],
) -> FreeRoomSuccessResponse:
    pass  # DB call
