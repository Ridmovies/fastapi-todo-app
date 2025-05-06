from datetime import datetime, time, timedelta

from sqlalchemy import Time, Interval
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class Todo(Base):
    __tablename__ = 'todo'
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    completed: Mapped[bool] = mapped_column(default=False)
    day: Mapped[datetime] = mapped_column(default=datetime.now)
    start_time: Mapped[time] = mapped_column(
        Time,
        default=time(9, 0),  # Дефолтное время: 09:00
        nullable=True
    )
    duration: Mapped[timedelta] = mapped_column(
        Interval,
        default=timedelta(hours=1),  # Дефолтная продолжительность: 1 час
        nullable=True
    )