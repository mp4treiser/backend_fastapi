import datetime
from typing import Annotated, AsyncGenerator
from sqlalchemy import String, text, create_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.core.config import settings

ASYNC_DATABASE_URL = f"postgresql+asyncpg://{settings.db.user}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.name}"
SYNC_DATABASE_URL = f"postgresql+psycopg2://{settings.db.user}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.name}"

sync_engine = create_engine(SYNC_DATABASE_URL, echo=False)
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)
sync_session_maker = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

def get_sync_session():
    with Session(sync_engine) as session:
        yield session


async def get_async_session():
    async with async_session_maker() as session:
        yield session

