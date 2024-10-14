from fastapi import Depends
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from db.repository.base import BaseRepository
from db.session import get_session


class UserRepository(BaseRepository):
    model = User
