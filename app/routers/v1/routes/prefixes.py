from fastapi import APIRouter, Depends
from typing import Annotated

from app.db.dependencies import get_db
from app.db.mongo_client import MongoORM
from app.schemas.params import PrefixesParams
from app.schemas import PrefixSuccessResponse

prefixes_router = APIRouter(prefix="/prefixes")


@prefixes_router.get("/", response_model=PrefixSuccessResponse)
async def get_prefixes(
    db: Annotated[MongoORM, Depends(get_db)],
    params: Annotated[PrefixesParams, Depends()],
) -> PrefixSuccessResponse:
    prefixes = await db.get_prefix_details(faculty=params.faculty)
    return PrefixSuccessResponse(data=prefixes)
