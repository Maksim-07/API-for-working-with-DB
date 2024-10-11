from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from core.config import settings

engine = create_async_engine(url=settings().postgres_dsn)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)


def get_db():
    db = async_session_maker()
    try:
        yield db
    finally:
        db.close()
