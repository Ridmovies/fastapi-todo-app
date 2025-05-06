from datetime import datetime

from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from src.todo.router import todo_list

page_router = APIRouter()


templates = Jinja2Templates(directory="src/templates")


@page_router.get("/todo")
async def get_todos_page(
    request: Request,
    todos=Depends(todo_list),
):
    return templates.TemplateResponse(
        name="todo_list.html",
        context={
            "request": request,
            "todos": todos,
            "current_date": datetime.now().strftime("%Y-%m-%d")  # Добавляем
        },
    )