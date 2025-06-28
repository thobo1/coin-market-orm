from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from orm.database import Base
from orm.mixins import RecordTimestamps
from orm.types import DEFAULT_LENGTH


class User(Base, RecordTimestamps):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(DEFAULT_LENGTH), nullable=True)
    email = Column(String(DEFAULT_LENGTH), nullable=True)
    is_onboarding = Column(Boolean, default=False)
    solana_address = Column(String(DEFAULT_LENGTH), unique=True, nullable=False)
    email_verified = Column(Boolean, default=False)
    email_otp = Column(String(6), nullable=True)
    email_otp_created_at = Column(DateTime, nullable=True)
    addresses = relationship("Address", back_populates="user")
    notes = relationship("Note", back_populates="user")

    @property
    def average_note(self):
        if self.notes:
            return sum(note.value for note in self.notes) / len(self.notes)
        return None
