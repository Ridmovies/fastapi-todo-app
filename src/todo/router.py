from fastapi import APIRouter
from starlette import status

from src.database import SessionDep
from src.todo.schemas import TodoCreate
from src.todo.service import TodoService

todo_router = APIRouter()

@todo_router.get("")
async def todo_list(session: SessionDep):
    return await TodoService.get_todo_list(session=session)


@todo_router.post("", status_code=status.HTTP_201_CREATED)
async def todo_create(session: SessionDep, todo_data: TodoCreate):
    return await TodoService.create_todo(session=session, todo_data=todo_data)


@todo_router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def todo_delete(session: SessionDep, todo_id: int):
    return await TodoService.delete_todo(session=session, todo_id=todo_id)


@todo_router.patch("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def toggle_todo_status(session: SessionDep, todo_id: int):
    return await TodoService.toggle_todo_status(session=session, todo_id=todo_id)