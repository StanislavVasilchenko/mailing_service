from fastapi import FastAPI
from src.notification.router import router as notify_router
import uvicorn


app = FastAPI()
app.include_router(notify_router)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
