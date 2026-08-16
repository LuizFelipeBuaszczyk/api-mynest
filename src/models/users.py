from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from infra.database import Base

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    is_superuser: Mapped[bool] = mapped_column()

    passwords: Mapped[list['Passwords']] = relationship(back_populates='owner')
