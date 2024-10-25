from sqlalchemy.orm import Session
from .models import Notify
from .schemas import NotifyCreate


class NotifyRepository:
    def __init__(self, session: Session):
        self.model = Notify
        self.db = session

    def save(self, notify: Notify):
        self.db.add(notify)
        self.db.commit()
        self.db.refresh(notify)

    def create(self, notify: NotifyCreate):
        notify = self.model(**notify.dict())
        self.save(notify)
        return notify

    def get_one(self, notify_id: int):
        return self.db.query(self.model).get(notify_id)
