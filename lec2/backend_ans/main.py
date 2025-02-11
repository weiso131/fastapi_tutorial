from fastapi import FastAPI

from routers.trick import router as trick_router

app = FastAPI()

app.include_router(trick_router, prefix="/trick")