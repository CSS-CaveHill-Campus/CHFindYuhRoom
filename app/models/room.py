from pydantic import BaseModel


class Room(BaseModel):
    room: str
    building: str
