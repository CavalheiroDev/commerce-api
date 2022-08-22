import uuid
from typing import Any, Tuple

from sqlalchemy import Table, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import as_declarative
from sqlalchemy.sql import func

from commerce_api.db.meta import meta


@as_declarative(metadata=meta)
class Base:
    """
    Base for all models.

    It has some type definitions to
    enhance autocompletion.
    """

    id = Column(
        'ID', UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    created = Column(
        'CREATED', DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    modified = Column(
        'MODIFIED', DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    __tablename__: str
    __table__: Table
    __table_args__: Tuple[Any, ...]
