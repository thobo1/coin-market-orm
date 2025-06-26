from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from orm.database import Base
from orm.mixins import RecordTimestamps


class Note(Base, RecordTimestamps):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)
    annonce_id = Column(Integer, ForeignKey("annonces.id"), nullable=False, unique=True)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    reviewer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller = relationship("User", back_populates="reviews_received", foreign_keys=[seller_id])
    reviewer = relationship("User", back_populates="reviews_given", foreign_keys=[reviewer_id])

    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="rating_check"),
    )
