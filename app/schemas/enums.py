"""All enums used by the application will be here!"""

from enum import Enum


class StatusEnum(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
