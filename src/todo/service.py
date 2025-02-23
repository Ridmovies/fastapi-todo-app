from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.todo.models import Todo
from src.todo.schemas import TodoCreate


class TodoService:

    @classmethod
    async def get_todo_list(cls, session: AsyncSession):
        query = select(Todo)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def create_todo(cls, session: AsyncSession, todo_data: TodoCreate):
        new_todo = Todo(**todo_data.model_dump())
        session.add(new_todo)
        await session.commit()
        return new_todo
