from sqlalchemy import (JSON, Boolean, Column, DateTime, ForeignKey, Index,
                        Integer, String, Text)
from sqlalchemy.orm import relationship

from orm.database import Base
from orm.mixins import RecordTimestamps


class Message(Base, RecordTimestamps):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id", ondelete="CASCADE"))
    sender_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    content = Column(Text, nullable=False)
    message_type = Column(String(20), default="text")  # text, image, file, system, location
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime, nullable=True)
    read_by = Column(JSON, nullable=True)  # {"user_id": "timestamp"}
    message_metadata = Column(JSON, nullable=True)  # Pour fichiers, images, etc.
    reply_to_id = Column(Integer, ForeignKey("messages.id"), nullable=True)  # Réponse à un message
    edited_at = Column(DateTime, nullable=True)
    is_edited = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # # Relations
    # conversation = relationship("Conversation", foreign_keys=[conversation_id], back_populates="messages")
    # sender = relationship("User", foreign_keys=[sender_id], backref="sent_messages")
    # reply_to = relationship("Message", remote_side=[id], backref="replies")
    # deleted_by_user = relationship("User", foreign_keys=[deleted_by])
    
    # Index pour les performances
    __table_args__ = (
        Index('idx_messages_conversation_created', 'conversation_id', 'created_at'),
        Index('idx_messages_sender', 'sender_id'),
        Index('idx_messages_unread', 'conversation_id', 'is_read'),
    )

