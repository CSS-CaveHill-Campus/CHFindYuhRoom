from fastapi import APIRouter, Query
from typing import Annotated

from app.schemas.params import ScheduleParams
from app.schemas import ScheduleSuccessResponse
from app.schemas.failure_response import FailureResponse
from app.schemas.success_response import SuccessResponse

schedule_router = APIRouter(prefix="/schedule")


@schedule_router.get("/", responses={404: {"model": FailureResponse}})
async def get_schedule(
    params: Annotated[ScheduleParams, Query()],
) -> ScheduleSuccessResponse:
    pass  # DB call
