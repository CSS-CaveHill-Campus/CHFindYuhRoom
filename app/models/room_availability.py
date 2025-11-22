from pydantic import BaseModel


class RoomAvailability(BaseModel):
    room: str
    day: str
    building: str | None
    available_from: int
    available_to: int
