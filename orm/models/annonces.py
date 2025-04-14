from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from orm.mixins import RecordTimestamps
from orm.database import Base
from sqlalchemy.orm import relationship


class Annonce(Base, RecordTimestamps):
    __tablename__ = "annonces"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
    publication_date = Column(DateTime, server_default=func.now())
    hash_url = Column(String(255), unique=True, nullable=False)
    photos = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    address_id = Column(Integer, ForeignKey("addresses.id"), nullable=True)
    status = Column(String(50), default="Not listed", nullable=False)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    pubkey = Column(String(44), unique=True, nullable=True)
