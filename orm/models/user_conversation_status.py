from sqlalchemy import (JSON, Boolean, Column, DateTime, ForeignKey, Index,
                        Integer, String, func, UniqueConstraint)
from sqlalchemy.orm import relationship

from orm.database import Base
from orm.mixins import RecordTimestamps


class UserConversationStatus(Base, RecordTimestamps):
    __tablename__ = "user_conversation_status"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    conversation_id = Column(Integer, ForeignKey("conversations.id", ondelete="CASCADE"))
    last_read_message_id = Column(Integer, ForeignKey("messages.id"), nullable=True)
    unread_count = Column(Integer, default=0)
    is_muted = Column(Boolean, default=False)
    is_pinned = Column(Boolean, default=False)
    last_activity_at = Column(DateTime, default=func.now())
    notification_preferences = Column(JSON, nullable=True)  # {"email": true, "push": true}
    custom_name = Column(String(255), nullable=True)  # Nom personnalisé pour la conversation
    
    # # Relations
    # user = relationship("User", backref="conversation_statuses")
    # conversation = relationship("Conversation")
    # last_read_message = relationship("Message")
    
    # Index pour les performances
    __table_args__ = (
        Index('idx_user_conversation_status_user', 'user_id'),
        Index('idx_user_conversation_status_conversation', 'conversation_id'),
        Index('idx_user_conversation_status_unread', 'user_id', 'unread_count'),
        Index('idx_user_conversation_status_activity', 'user_id', 'last_activity_at'),
        # Contrainte unique pour éviter les doublons
        UniqueConstraint('user_id', 'conversation_id', name='uq_user_conversation_status'),
    )
