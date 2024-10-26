from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from src.database import Base


class Logs(Base):
    __tablename__ = "logs"

    logs_id = Column(Integer, primary_key=True, autoincrement=True)
    sent_at = Column(DateTime, default=datetime.now(), nullable=False)
    email = Column(String(length=50), nullable=True)
    telegram = Column(String(length=50), nullable=True)
    sent = Column(Boolean(), default=True, nullable=False)
