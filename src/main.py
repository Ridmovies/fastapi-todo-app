from fastapi import FastAPI
from src.dev.router import dev_router
from src.todo.router import todo_router

app = FastAPI()
app.include_router(todo_router, prefix="/todo", tags=["todo"])
app.include_router(dev_router, prefix="/dev", tags=["dev"])


