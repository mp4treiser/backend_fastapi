from sqlalchemy.orm import Mapped
from src.core.orm.base import Base, str_255, bool_default_false, bool_default_true, str_255_unique


class User(Base):
    __tablename__ = "users"

    email: Mapped[str_255_unique]
    password: Mapped[str_255]
    first_name: Mapped[str_255]
    last_name: Mapped[str_255]
    is_superuser: Mapped[bool_default_false]
    is_active: Mapped[bool_default_true]
