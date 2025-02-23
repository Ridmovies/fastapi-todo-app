from datetime import datetime

from pydantic import BaseModel

class TodoBase(BaseModel):
    text: str

class TodoCreate(TodoBase):
    pass

class TodoOut(TodoBase):
    id: int
    created_at: datetime
    completed: bool