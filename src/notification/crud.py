from sqlalchemy.orm import Session
from .schemas import NotifyCreate
from .repository import NotifyRepository
from src.tasks.task_notify import send_notification
from .constants import DELAY_DAY, DELAY_HOUR
from .models import Notify


async def create_notify(notify: NotifyCreate, db: Session) -> Notify:
    repo = NotifyRepository(session=db)
    notify_db = repo.create(notify)

    match notify_db.delay:
        case 0:
            send_notification.delay(notify_db.notify_id)
        case 1:
            send_notification.apply_async(
                args=[notify_db.notify_id], countdown=DELAY_HOUR
            )
        case 2:
            send_notification.apply_async(
                args=[notify_db.notify_id], countdown=DELAY_DAY
            )

    return notify_db
