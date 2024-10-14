from fastapi import APIRouter, Depends

from services.user import UserService
from schemas.user import UserSchema, UserUpdateSchema

user_router = APIRouter(prefix="/users", tags=["CRUD operation"])


@user_router.get("/{user_id}")
async def get_user(user_id: int, user_service: UserService = Depends()):
    result = await user_service.get_user(user_id)
    return result


@user_router.post("")
async def post_user(user_schema: UserSchema, user_service: UserService = Depends()):
    result = await user_service.insert(email=user_schema.email, password=user_schema.password, name=user_schema.name,
                                       city=user_schema.city)
    return result


@user_router.put("/{user_id}")
async def put_user(user_id: int, user_update: UserUpdateSchema, user_service: UserService = Depends()):
    result = await user_service.update(data_id=user_id, email=user_update.email, password=user_update.password,
                                       name=user_update.name,
                                       city=user_update.city)
    return result


@user_router.delete("/{user_id}")
async def delete_user(user_id: int, user_service: UserService = Depends()):
    result = await user_service.delete(user_id)
    return result
