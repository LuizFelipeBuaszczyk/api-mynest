import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from model import Base

class Password(Base):
    __tablename__ = 'password'

    id = Column(
        UUID(as_uuid=True), 
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        )
    
    title = Column(
        String(50),
        nullable=False
    )
    
    password = Column(
        String(250),
        nullable=False
    )

    fk_id_user = Column(
        UUID(as_uuid=True),
        ForeignKey('user.id')
    )