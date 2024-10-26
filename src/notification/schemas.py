from pydantic import BaseModel


class NotifyBase(BaseModel):
    message: str
    recipient: str | list[str]
    delay: int = 0


class NotifyCreate(NotifyBase):
    pass


class NotifyOut(NotifyBase):
    pass
