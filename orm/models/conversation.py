from sqlalchemy import (JSON, Boolean, Column, DateTime, ForeignKey, Index,
                        Integer, String)
from sqlalchemy.orm import relationship

from orm.database import Base
from orm.mixins import RecordTimestamps


class Conversation(Base, RecordTimestamps):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    annonce_id = Column(Integer, ForeignKey("annonces.id", ondelete="CASCADE"))
    buyer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    seller_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String(255), nullable=True)  # Titre personnalisé de la conversation
    last_message_at = Column(DateTime, nullable=True)
    last_message_id = Column(Integer, ForeignKey("messages.id"), nullable=True)
    is_active = Column(Boolean, default=True)
    is_archived = Column(Boolean, default=False)
    archived_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    archived_at = Column(DateTime, nullable=True)
    settings = Column(JSON, nullable=True)  # {"muted": false, "auto_archive": true}
    
    # Relations
    annonce = relationship("Annonce", backref="conversations")
    buyer = relationship("User", foreign_keys=[buyer_id], backref="buyer_conversations")
    seller = relationship("User", foreign_keys=[seller_id], backref="seller_conversations")
    messages = relationship("Message", foreign_keys="[Message.conversation_id]", back_populates="conversation", cascade="all, delete-orphan")
    last_message = relationship("Message", foreign_keys=[last_message_id])
    archived_by_user = relationship("User", foreign_keys=[archived_by])
    
    # Index pour les performances
    __table_args__ = (
        Index('idx_conversations_users', 'buyer_id', 'seller_id'),
        Index('idx_conversations_annonce', 'annonce_id'),
        Index('idx_conversations_last_message', 'last_message_at'),
        Index('idx_conversations_active', 'is_active', 'is_archived'),
    )
