from fastapi import APIRouter
from sqlalchemy import text

from src.database import async_engine, Base, SessionDep

dev_router = APIRouter()

@dev_router.post("/create_db")
async def create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    return { "message": "Database created"}

@dev_router.get("/check_db")
async def check_db(session: SessionDep):
    await session.execute(text("SELECT 1"))
    return { "message": "Database is ready"}
