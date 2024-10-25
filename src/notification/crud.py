from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .schemas import NotifyCreate
from .repository import NotifyRepository
from src.tasks.task_notify import send_notification


async def create_notify(notify: NotifyCreate, db: Session):
    if notify.delay not in [0, 1, 2]:
        raise HTTPException(
            detail="delay cannot be greater than 2",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    repo = NotifyRepository(session=db)
    notify_db = repo.create(notify)

    match notify_db.delay:
        case 0:
            send_notification.delay(notify_db.notify_id)
        case 1:
            send_notification.apply_async(args=[notify_db.notify_id], countdown=60)
        case 2:
            send_notification.apply_async(args=[notify_db.notify_id], countdown=120)

    return notify_db
