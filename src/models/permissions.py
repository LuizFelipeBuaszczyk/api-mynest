from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from infra.database import Base

class Permissions(Base):
    __tablename__ = 'permissions'

    id: Mapped[int] = mapped_column(primary_key=True)
    codename: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(String(255))