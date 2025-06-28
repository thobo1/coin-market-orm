from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from orm.database import Base
from orm.mixins import RecordTimestamps


class Note(Base, RecordTimestamps):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    annonce_id = Column(Integer, ForeignKey("annonces.id"), nullable=False)
    user = relationship("User", back_populates="notes")
    # annonce = relationship("Annonce", back_populates="note", uselist=False)
    __table_args__ = (
        CheckConstraint("value >= 1 AND value <= 5", name="note_value_range_check"),
    )
