from sqlalchemy.orm import Session
from src.tasks.settings import celery_app
from src.notification.utils import send_mail, send_to_telegram
from src.notification.repository import NotifyRepository
from src.database import get_db


@celery_app.task
def send_notification(notify_id: int, session: Session = get_db().__next__()):
    repo = NotifyRepository(session=session)
    notify_db = repo.get_one(notify_id)

    recipient = (
        notify_db.recipient
        if isinstance(notify_db.recipient, list)
        else [notify_db.recipient]
    )
    for address in recipient:
        if address.isdigit():
            send_to_telegram(telegram_id=address, message_text=notify_db.message)
        elif "@" in address:
            send_mail(receiver_email=address, message_text=notify_db.message)
