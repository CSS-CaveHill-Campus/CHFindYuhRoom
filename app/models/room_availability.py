from pydantic import BaseModel


class RoomAvailability(BaseModel):
    room: str
    day: str
    available_from: int
    available_to: int
