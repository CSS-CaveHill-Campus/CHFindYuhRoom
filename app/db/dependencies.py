"""This file will contain all of the dependencies that the project needs"""

from fastapi import Request
from app.db.mongo_client import MongoORM


def get_db(request: Request) -> MongoORM:
    return request.app.state.db
