from fastapi import APIRouter, Depends
from typing import Annotated

from app.schemas.params import PrefixesParams
from app.schemas import PrefixSuccessResponse
from app.schemas.failure_response import FailureResponse

prefixes_router = APIRouter(prefix="/prefixes")


@prefixes_router.get("/", response_model=PrefixSuccessResponse, responses={404: {"model": FailureResponse}})
async def get_prefixes(
    params: Annotated[PrefixesParams, Depends()],
) -> PrefixSuccessResponse:
    pass  # DB call
