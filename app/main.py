from fastapi import FastAPI
from app.routers import v1_router

app = FastAPI(title="UWI FindYuhRoom API")


app.include_router(router=v1_router)


@app.get("/")
async def index():
    return "Hello world!"
