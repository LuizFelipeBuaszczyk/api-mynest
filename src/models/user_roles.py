from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from infra.database import Base

class UserRoles(Base):
    __tablename__ = 'user_roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    fk_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    fk_role: Mapped[int] = mapped_column(ForeignKey('roles.id'))
