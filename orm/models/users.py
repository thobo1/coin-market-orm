from sqlalchemy import Column, Integer, Boolean, String
from orm.database import Base
from orm.mixins import RecordTimestamps
from orm.types import DEFAULT_LENGTH
from sqlalchemy.orm import relationship


class User(Base, RecordTimestamps):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(DEFAULT_LENGTH), nullable=True)
    is_onboarding = Column(Boolean, default=False)
    solana_address = Column(String(DEFAULT_LENGTH), unique=True, nullable=False)
    addresses = relationship("Address", back_populates="user")
    notes = relationship("Note", back_populates="user")

    @property
    def average_note(self):
        if self.notes:
            return sum(note.value for note in self.notes) / len(self.notes)
        return None
