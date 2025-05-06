from datetime import datetime, date

from pydantic import BaseModel

class TodoBase(BaseModel):
    text: str

class TodoCreate(BaseModel):
    text: str
    day: date | None = None  # Опционально (дефолт в модели)
    start_time: str | None = None  # Формат "HH:MM"
    duration: int | None = None  # В минутах (опционально)

class TodoOut(TodoBase):
    id: int
    created_at: datetime
    completed: bool