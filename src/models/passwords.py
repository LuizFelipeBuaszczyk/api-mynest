from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from infra.database import Base

class Passwords(Base):
    __tablename__ = 'passwords'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    fk_owner: Mapped[int] = mapped_column(ForeignKey('users.id'))

    owner: Mapped['Users'] = relationship(back_populates='passwords')
