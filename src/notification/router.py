from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .schemas import NotifyCreate, NotifyOut
from src.database import get_db
from . import crud


router = APIRouter(prefix="/api/notify", tags=["Notify"])


@router.post("", response_model=NotifyOut)
async def create_notify(notify: NotifyCreate, db: Session = Depends(get_db)):
    return await crud.create_notify(notify=notify, db=db)
