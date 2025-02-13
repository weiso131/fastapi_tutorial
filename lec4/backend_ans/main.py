from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers.trick import router as trick_router
from routers.auth import router as auth_router
from database.database import init_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("初始化資料庫")
    await init_database()
    yield
    print("關閉應用")

app = FastAPI(lifespan=lifespan)

app.include_router(trick_router, prefix="/trick")
app.include_router(auth_router, prefix="/auth")