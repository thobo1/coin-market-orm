from math import factorial
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text, false
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from orm.database import Base
from orm.mixins import RecordTimestamps
from orm.types import DEFAULT_LENGTH


class User(Base, RecordTimestamps):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # username = Column(String(DEFAULT_LENGTH), nullable=True)
    # email = Column(String(DEFAULT_LENGTH), nullable=True)
    # is_onboarding = Column(Boolean, default=false)
    solana_address = Column(String(DEFAULT_LENGTH), unique=True, nullable=False)
    is_banned = Column(Boolean, default=false, nullable=False)
    ban_expires_at = Column(DateTime, nullable=True)
    ban_reason = Column(Text, nullable=True)
    # email_verified = Column(Boolean, default=false)
    # email_otp = Column(String(6), nullable=True)
    # email_otp_created_at = Column(DateTime, nullable=True)

    addresses = relationship("Address", back_populates="user")
    
    reviews_received = relationship("Note", back_populates="seller", foreign_keys="[Note.seller_id]")
    reviews_given = relationship("Note", back_populates="reviewer", foreign_keys="[Note.reviewer_id]")

    @property
    def average_note(self):
        if self.reviews_received:
            return sum(note.rating for note in self.reviews_received) / len(self.reviews_received)
        return None
