"""Schema for a successful response"""

from typing import Any
from pydantic import BaseModel

from app.schemas.enums import StatusEnum


class SuccessResponse(BaseModel):
    status: StatusEnum = StatusEnum.SUCCESS
    data: list[Any]


class ScheduleSuccessResponse(SuccessResponse):
    data: list[Schedule]


class FreeRoomSuccessResponse(SuccessResponse):
    data: list[FreeRoom]


class RoomSuccessResponse(SuccessResponse):
    data: list[Room]


class PrefixSuccessResponse(SuccessResponse):
    data: list[Prefix]
