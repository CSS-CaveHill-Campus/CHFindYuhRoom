from fastapi import FastAPI

app = FastAPI(title="UWI FindYuhRoom API")


@app.get("/")
async def index():
    return "Hello world!"
