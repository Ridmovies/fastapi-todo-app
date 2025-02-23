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

    #
    # @classmethod
    # async def update_todo(cls, session: AsyncSession, todo_id: int, todo_data: TodoCreate):
    #     query = select(Todo).where(Todo.id == todo_id)
    #     result = await session.execute(query)
    #     todo = result.scalars().first()
    #     if not todo:
    #         return
