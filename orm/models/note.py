from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from orm.database import Base
from orm.mixins import RecordTimestamps
from sqlalchemy.orm import relationship
from orm.models.users import User
from orm.models.annonces import Annonce


class Note(Base, RecordTimestamps):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    annonce_id = Column(Integer, ForeignKey("annonces.id"), nullable=False)
    user = relationship("User", back_populates="notes")
    # annonce = relationship("Annonce", back_populates="notes")
    __table_args__ = (
        CheckConstraint("value >= 1 AND value <= 5", name="note_value_range_check"),
    )
