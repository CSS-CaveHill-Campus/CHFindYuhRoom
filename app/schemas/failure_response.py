"""Schema for failure responses"""

from pydantic import BaseModel

from app.schemas.enums import StatusEnum
from app.schemas.error import AppError


class FailureResponse(BaseModel):
    status: StatusEnum = StatusEnum.FAILURE
    error: AppError
