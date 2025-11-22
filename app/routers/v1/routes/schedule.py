from fastapi import APIRouter, Depends, Request
from typing import Annotated

from app.db.mongo_client import MongoORM
from app.schemas.params import ScheduleParams
from app.schemas import ScheduleSuccessResponse
from app.schemas.failure_response import FailureResponse

schedule_router = APIRouter(prefix="/schedule")


@schedule_router.get(
    "/",
    response_model=ScheduleSuccessResponse,
)
async def get_schedule(
    request: Request,
    params: Annotated[ScheduleParams, Depends()],
) -> ScheduleSuccessResponse:
    db: MongoORM = request.app.state.db
    schedules = await db.get_schedules(**params.model_dump())
    return ScheduleSuccessResponse(data=schedules)
