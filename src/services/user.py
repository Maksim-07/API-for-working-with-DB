from fastapi import Depends

from core.exceptions import user_not_found_exception
from db.repository.user import UserRepository
from schemas.user import UserSchema


class UserService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self._user_repository = user_repository

    async def get_user(self, user_id) -> UserSchema:
        user = await self._user_repository.find_one_or_none_by_id(data_id=user_id)

        if not user:
            raise user_not_found_exception

        return user

    async def insert(self, **kwargs):
        await self._user_repository.add(**kwargs)

    async def update(self, data_id: int, **kwargs):
        await self._user_repository.update(data_id=data_id, **kwargs)

    async def delete(self, data_id: int):
        await self._user_repository.delete(data_id=data_id)
