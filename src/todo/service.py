from datetime import time

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.todo.models import Todo
from src.todo.schemas import TodoCreate


class TodoService:

    @classmethod
    async def get_todo_list(cls, session: AsyncSession):
        # Сначала сортируем по дате (ближайшие вверху), затем по времени
        query = select(Todo).order_by(
            Todo.day.asc(),  # Сначала ближайшие даты
            Todo.start_time.asc()  # Для одинаковых дат - раньшее время вверху
        )
        result = await session.execute(query)
        return result.scalars().all()


    @classmethod
    async def create_todo(cls, session: AsyncSession, todo_data: TodoCreate):
        # Преобразуем строку времени в объект time
        if todo_data.start_time:
            try:
                hours, minutes = map(int, todo_data.start_time.split(':'))
                todo_data.start_time = time(hour=hours, minute=minutes)
            except (ValueError, AttributeError):
                todo_data.start_time = None  # или установите дефолтное значение
        new_todo = Todo(**todo_data.model_dump())
        session.add(new_todo)
        await session.commit()
        return new_todo


    @classmethod
    async def delete_todo(cls, session: AsyncSession, todo_id: int):
        query = select(Todo).where(Todo.id == todo_id)
        result = await session.execute(query)
        todo = result.scalar_one_or_none()
        if not todo:
            return None
        await session.delete(todo)
        await session.commit()
        return {"message": "todo deleted"}


    @classmethod
    async def change_status_todo(cls, session: AsyncSession, todo_id: int):
        query = select(Todo).where(Todo.id == todo_id)
        result = await session.execute(query)
        todo = result.scalar_one_or_none()
        if not todo:
            return None
        todo.completed = False if todo.completed else True
        await session.commit()


    @classmethod
    async def toggle_todo_status(cls, session: AsyncSession, todo_id: int):
        query = select(Todo).where(Todo.id == todo_id)
        result = await session.execute(query)
        todo = result.scalar_one_or_none()

        if not todo:
            raise HTTPException(status_code=404, detail="Task not found")

        todo.completed = not todo.completed
        await session.commit()
        return todo

