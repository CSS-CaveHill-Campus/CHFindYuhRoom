"""This will contain the format for parameters to be used by the routes"""

from pydantic import BaseModel, Field

from schemas.enums import FacultyEnum, DayEnum


class ScheduleParams(BaseModel):
    faculty: FacultyEnum | None = Field(
        None, description="Faculty to search for classes under"
    )
    limit: int | None = Field(
        20,
        description="How many results to return. Will default to 20. Setting limit to 0 will return ALL results.",
    )
    day: DayEnum | None = Field(
        None,
        description="3 letter weekday of which to return the schedule for (Mon, Tue, Wed, Thu). Will default to all.",
    )
    room: str | None = Field(
        None,
        description="A specific room to check the schedule for. Will default to all. Refer to /rooms for a list of all rooms.",
    )
    prefix: str | None = Field(
        None,
        description="4 character Course prefix (Example: PSCY, COMP, MATH) to filter by.",
    )


class FreeRoomParams(BaseModel):
    day: DayEnum = Field(..., description="The day to check for.")
    hour: int | None = Field(
        None, description="Hour in 24 hour format to check for room availabilities."
    )
    duration: int | None = Field(
        1,
        description="Number of hours a room should be available for, in order to be shown. Will default to 1, IF hour is set.",
    )
    room: str | None = Field(
        None, description="A specific room to check for. (Refer to /rooms)"
    )


class PrefixesParams(BaseModel):
    faculty: FacultyEnum | None = Field(
        None, description="Optional parameter to filter prefixes by faculty."
    )
