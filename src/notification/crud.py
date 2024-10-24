from sqlalchemy.orm import Session

from .schemas import NotifyCreate
from .repository import NotifyRepository


async def create_notify(notify: NotifyCreate, db: Session):
    repo = NotifyRepository(session=db)
    notify_db = repo.create(notify)

    return notify_db
