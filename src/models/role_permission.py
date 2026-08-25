from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from infra.database import Base

class RolePermission(Base):
    __tablename__ = 'role_permissions'

    id: Mapped[int] = mapped_column(primary_key=True)
    fk_permission: Mapped[int] = mapped_column(ForeignKey('permissions.id'))
    fk_role: Mapped[int] = mapped_column(ForeignKey('roles.id'))
