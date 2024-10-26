from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .schemas import NotifyCreate, NotifyOut
from src.database import get_db
from . import crud


router = APIRouter(prefix="/api", tags=["Notify"])


@router.post(
    "/notify/",
    response_model=NotifyOut,
    description="When a notification is created, automatic sending begins with the specified delay. "
    "0 - SEND NOW, 1 - SEND IN AN HOUR, 2 - SEND TOMORROW",
    summary="Created Notify",
)
async def create_notify(notify: NotifyCreate, db: Session = Depends(get_db)):
    if notify.delay not in (0, 1, 2):
        raise HTTPException(
            detail="The delay parameter should be in the range from 0 to 2",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return await crud.create_notify(notify=notify, db=db)
