from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.sql import func

from orm.database import Base
from orm.mixins import RecordTimestamps


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
    address = Column(JSON, nullable=True)
    status = Column(String(50), default="Not listed", nullable=False)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    pubkey = Column(String(44), unique=True, nullable=True)
    shipment_confirmation = Column(JSON, nullable=True)
    dispute = Column(JSON, nullable=True)
    shipping_regions = Column(JSON, nullable=True)