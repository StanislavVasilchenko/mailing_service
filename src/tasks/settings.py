from celery import Celery
from private_keys import BROKER_REDIS_URL

celery_app = Celery(
    "tasks",
    broker=BROKER_REDIS_URL,
    include=["src.tasks.task_notify"],
)
