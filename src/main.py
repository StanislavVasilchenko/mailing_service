from fastapi import FastAPI
from src.notification.router import router as notify_router

app = FastAPI()
app.include_router(notify_router)


@app.get("/")
async def hello():
    return {"message": "hello_world"}
