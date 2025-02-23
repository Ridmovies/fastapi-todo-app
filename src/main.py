from fastapi import FastAPI
from src.dev.router import dev_router
from src.todo.router import todo_router
from src.pages.router import page_router

app = FastAPI()
app.include_router(todo_router, prefix="/todo", tags=["todo"])
app.include_router(page_router, prefix="/pages", tags=["pages"])
app.include_router(dev_router, prefix="/dev", tags=["dev"])


