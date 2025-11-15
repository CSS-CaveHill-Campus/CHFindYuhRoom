"""Application specfic errors will be created here"""

from pydantic import BaseModel


class AppError(BaseModel):
    code: int
    message: str
    type: str
