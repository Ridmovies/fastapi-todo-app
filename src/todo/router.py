from fastapi import APIRouter

from src.database import SessionDep
from src.todo.schemas import TodoCreate
from src.todo.service import TodoService

todo_router = APIRouter()

@todo_router.get("")
async def todo_list(session: SessionDep):
    return await TodoService.get_todo_list(session=session)


@todo_router.post("")
async def todo_create(session: SessionDep, todo_data: TodoCreate):
    return await TodoService.create_todo(session=session, todo_data=todo_data)