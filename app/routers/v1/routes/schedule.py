from fastapi import APIRouter, Depends
from typing import Annotated

from app.db.dependencies import get_db
from app.db.mongo_client import MongoORM
from app.schemas.params import ScheduleParams
from app.schemas import ScheduleSuccessResponse

schedule_router = APIRouter(prefix="/schedule")


@schedule_router.get(
    "/",
    response_model=ScheduleSuccessResponse,
)
async def get_schedule(
    db: Annotated[MongoORM, Depends(get_db)],
    params: Annotated[ScheduleParams, Depends()],
) -> ScheduleSuccessResponse:
    schedules = await db.get_schedules(
        faculty=params.faculty,
        day=params.day,
        room=params.room,
        prefix=params.prefix,
        **(
            {"limit": params.limit}
            if params.limit is not None
            else {}
        ),
    )
    return ScheduleSuccessResponse(data=schedules)
