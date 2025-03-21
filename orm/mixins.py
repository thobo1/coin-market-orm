from sqlalchemy import TIMESTAMP, Column
from sqlalchemy.sql import func


class RecordTimestamps:
    updated_at = Column(
        TIMESTAMP,
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
        doc="Timestamp when the record was last updated",
    )
    created_at = Column(
        TIMESTAMP,
        default=func.now(),
        nullable=False,
        doc="Timestamp when the record was created",
    )
