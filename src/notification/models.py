from sqlalchemy import Column, Integer, String, JSON
from database import Base


class Notify(Base):
    __tablename__ = "notification"

    notify_id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(length=1024), nullable=False)
    recipient = Column(JSON)
    delay = Column(Integer)
