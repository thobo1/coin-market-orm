import os
from contextlib import contextmanager
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv()

Base = declarative_base()


class Database:
    def __init__(self, url: str = None):
        self._engine = create_engine(
            url or os.getenv("DATABASE_URL"), echo=bool(os.getenv("SQL_ECHO", False))
        )
        self._session_factory = sessionmaker(
            bind=self._engine, autocommit=False, autoflush=False
        )
        self._scoped_session = scoped_session(self._session_factory)

    def create_database(self) -> None:
        """Crée toutes les tables définies dans les modèles"""
        Base.metadata.create_all(self._engine)

    def drop_database(self) -> None:
        """Supprime toutes les tables"""
        Base.metadata.drop_all(self._engine)

    @contextmanager
    def session(self) -> Generator:
        """Crée un contexte de session pour les opérations de base de données"""
        session = self._scoped_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @property
    def engine(self):
        return self._engine
