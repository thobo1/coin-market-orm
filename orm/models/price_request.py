from sqlalchemy import (JSON, Column, DateTime, Float, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.sql import func

from orm.database import Base
from orm.mixins import RecordTimestamps


class PriceRequest(Base, RecordTimestamps):
    __tablename__ = "price_requests"

    id = Column(Integer, primary_key=True, index=True)
    annonce_id = Column(Integer, ForeignKey("annonces.id"))
    buyer_id = Column(Integer, ForeignKey("users.id")) 
    seller_id = Column(Integer, ForeignKey("users.id")) 
    last_offer_by = Column(String)
    offer_price = Column(Float)
    signature = Column(String, nullable=True)
    status = Column(String)
    timestamp = Column(DateTime, default=func.now())  