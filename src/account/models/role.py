from typing import List

from sqlalchemy.orm import Mapped, relationship

from src.core.orm.base import Base, str_255_unique


class Role(Base):
    __tablename__ = "roles"

    name: Mapped[str_255_unique]
    users: Mapped[List["User"]] = relationship(back_populates="role")