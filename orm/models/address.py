from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Index
from orm.database import Base
from orm.mixins import RecordTimestamps
from sqlalchemy.orm import relationship
from orm.models.users import User


class Address(Base, RecordTimestamps):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipient = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_default = Column(Boolean, default=False, nullable=False)
    user = relationship("User", back_populates="addresses")
    __table_args__ = (
        Index(
            "uq_user_default_address",
            "user_id",
            unique=True,
            postgresql_where=(is_default == True),
        ),
    )
