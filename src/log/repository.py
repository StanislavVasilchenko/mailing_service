from sqlalchemy.orm import Session

from src.log.models import Logs


class LogsRepositories:
    def __init__(self, session: Session):
        self.model = Logs
        self.session = session

    def save(self, logs: Logs):
        self.session.add(logs)
        self.session.commit()
        self.session.refresh(logs)
