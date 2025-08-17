from sqlalchemy import (JSON, Boolean, Column, DateTime, ForeignKey, Index,
                        Integer, String, Text)
from sqlalchemy.orm import relationship

from orm.database import Base
from orm.mixins import RecordTimestamps


class Notification(Base, RecordTimestamps):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    notification_type = Column(String(50), nullable=False)  # new_message, new_conversation, price_offer, etc.
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime, nullable=True)
    data = Column(JSON, nullable=True)  # Données supplémentaires
    priority = Column(String(20), default="normal")  # low, normal, high, urgent
    category = Column(String(50), nullable=True)  # chat, transaction, system, etc.
    action_url = Column(String(500), nullable=True)  # URL pour redirection
    expires_at = Column(DateTime, nullable=True)  # Expiration de la notification
    sent_via = Column(JSON, nullable=True)  # {"email": true, "push": true, "in_app": true}
    external_id = Column(String(255), nullable=True)  # ID externe (Firebase, etc.)
    
    # Relations
    user = relationship("User", backref="notifications")
    
    # Index pour les performances
    __table_args__ = (
        Index('idx_notifications_user_unread', 'user_id', 'is_read'),
        Index('idx_notifications_type', 'notification_type'),
        Index('idx_notifications_priority', 'priority'),
        Index('idx_notifications_created', 'user_id', 'created_at'),
    )