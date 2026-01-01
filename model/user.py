import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from model import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(
        UUID(as_uuid=True), 
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        )
    
    username = Column(
        String(50),
        unique=True,
        nullable=False,
    )

    password = Column(
        String(250),
        nullable=False
    )
