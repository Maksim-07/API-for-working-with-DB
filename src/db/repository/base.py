from fastapi import Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_session


class BaseRepository:
    model = None
    _session: AsyncSession

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self._session = session

    async def find_one_or_none_by_id(self, data_id: int):
        query = select(self.model).filter_by(id=data_id)
        result = await self._session.execute(query)
        return result.scalar_one_or_none()

    async def add(self, **kwargs):
        new_instance = insert(self.model).values(**kwargs)
        await self._session.execute(new_instance)
        await self._session.commit()

    async def update(self, data_id: int, **kwargs):
        new_instance = update(self.model).values(**kwargs).filter_by(id=data_id)
        await self._session.execute(new_instance)
        await self._session.commit()

    async def delete(self, data_id: int):
        new_instance = delete(self.model).filter_by(id=data_id)
        await self._session.execute(new_instance)
        await self._session.commit()
