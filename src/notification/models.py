from fastapi import HTTPException, status
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import validates
from src.database import Base
from .constants import LENGTH_EMAIL


class Notify(Base):
    __tablename__ = "notification"

    notify_id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(length=1024), nullable=False)
    recipient = Column(JSON)
    delay = Column(Integer, default=0)

    @validates("recipient")
    def validate_recipient(self, key, value):
        if isinstance(value, list):
            for rec in value:
                if len(rec) > LENGTH_EMAIL:
                    raise HTTPException(
                        detail=f"Длина адреса {rec} больше {LENGTH_EMAIL}",
                        status_code=status.HTTP_400_BAD_REQUEST,
                    )
        if isinstance(value, str) and len(value) > LENGTH_EMAIL:
            raise HTTPException(
                detail=f"Длина адреса {value} больше {LENGTH_EMAIL}",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return value
