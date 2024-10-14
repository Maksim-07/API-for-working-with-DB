from fastapi import APIRouter

from api.crud import user_router

crud_router = APIRouter(prefix="/crud")
crud_router.include_router(user_router)
