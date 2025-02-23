from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.dev.router import dev_router
from src.todo.router import todo_router
from src.pages.router import page_router

app = FastAPI()
app.include_router(todo_router, prefix="/todo", tags=["todo"])
app.include_router(page_router, prefix="/pages", tags=["pages"])
app.include_router(dev_router, prefix="/dev", tags=["dev"])


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)