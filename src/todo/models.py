from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class Todo(Base):
    __tablename__ = 'todo'
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    completed: Mapped[bool] = mapped_column(default=False)