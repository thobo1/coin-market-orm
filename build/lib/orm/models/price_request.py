from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from orm.database import Base
from orm.mixins import RecordTimestamps


class PriceRequest(Base, RecordTimestamps):
    __tablename__ = "price_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    annonce_id = Column(Integer, ForeignKey("annonces.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    signature = Column(Text, nullable=True)
    offered_price = Column(Float, nullable=True)
    status = Column(String(50), default="Pending", nullable=False)
