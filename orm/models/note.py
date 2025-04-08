from sqlalchemy import Column, Integer, ForeignKey
from orm.database import Base
from orm.mixins import RecordTimestamps
from sqlalchemy.orm import relationship
from orm.models.users import User
from orm.models.annonces import Annonce


class Note(Base, RecordTimestamps):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Integer, nullable=False)  # La note (entre 1 et 5, en entier)
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # L'utilisateur noté
    annonce_id = Column(
        Integer, ForeignKey("annonces.id"), nullable=False
    )  # L'annonce associée
    user = relationship("User", back_populates="notes")  # Relation inverse vers User
    annonce = relationship(
        "Annonce", back_populates="notes"
    )  # Relation inverse vers Annonce
