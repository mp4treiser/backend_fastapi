import datetime

from typing import Annotated, AsyncGenerator
from sqlalchemy import String, text, create_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.core.config import settings

str_255 = Annotated[str, mapped_column(String(255), nullable=True)]
str_255_unique = Annotated[str, mapped_column(String(255), nullable=False, unique=True)]
bool_default_true = Annotated[bool, mapped_column(default=True)]
bool_default_false = Annotated[bool, mapped_column(default=False)]
date = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    created_at: Mapped[date]
    update_at: Mapped[date]