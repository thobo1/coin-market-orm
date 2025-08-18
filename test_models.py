#!/usr/bin/env python3
"""
Script de test rapide pour valider les modèles SQLAlchemy
Usage: python test_models.py
"""

import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ajouter le répertoire courant au path pour importer les modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from orm.database import Base
from orm.models import *  # Importe tous les modèles


def test_model_initialization():
    """Teste l'initialisation de tous les modèles"""
    print("🔍 Test d'initialisation des modèles...")
    
    try:
        # Vérifier que tous les modèles peuvent être importés
        models = [
            User, Annonce, Conversation, Message, Address, 
            Note, Notification, PriceRequest, UserConversationStatus, GlobalSetting
        ]
        
        print(f"✅ {len(models)} modèles importés avec succès")
        
        # Vérifier que chaque modèle a une table définie
        for model in models:
            if hasattr(model, '__tablename__'):
                print(f"  ✅ {model.__name__} -> {model.__tablename__}")
            else:
                print(f"  ❌ {model.__name__} n'a pas de __tablename__")
                
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'import des modèles: {e}")
        return False


def test_database_creation():
    """Teste la création de la base de données en mémoire"""
    print("\n🗄️  Test de création de base de données...")
    
    try:
        # Créer une base de données SQLite en mémoire pour les tests
        engine = create_engine("sqlite:///:memory:", echo=False)
        
        # Créer toutes les tables
        Base.metadata.create_all(engine)
        print("✅ Tables créées avec succès")
        
        # Vérifier que toutes les tables existent
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"✅ {len(tables)} tables créées: {', '.join(tables)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création des tables: {e}")
        return False


def test_relationships():
    """Teste les relations entre les modèles"""
    print("\n🔗 Test des relations...")
    
    try:
        # Créer une session de test
        engine = create_engine("sqlite:///:memory:", echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Test de création d'objets avec relations
        user = User(
            username="test_user",
            email="test@example.com",
            solana_address="test_solana_address_123"
        )
        session.add(user)
        session.flush()  # Pour obtenir l'ID
        
        annonce = Annonce(
            title="Test Annonce",
            description="Test Description",
            price=100.0,
            category="Test",
            hash_url="test_hash_123",
            user_id=user.id
        )
        session.add(annonce)
        session.flush()
        
        conversation = Conversation(
            annonce_id=annonce.id,
            buyer_id=user.id,
            seller_id=user.id,
            title="Test Conversation"
        )
        session.add(conversation)
        session.flush()
        
        message = Message(
            conversation_id=conversation.id,
            sender_id=user.id,
            content="Test message"
        )
        session.add(message)
        session.flush()
        
        print("✅ Relations testées avec succès")
        session.close()
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test des relations: {e}")
        return False


def main():
    """Fonction principale de test"""
    print("🚀 Démarrage des tests des modèles SQLAlchemy\n")
    
    tests = [
        test_model_initialization,
        test_database_creation,
        test_relationships
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Erreur inattendue dans {test.__name__}: {e}")
    
    print(f"\n📊 Résultats: {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! Vos modèles sont prêts.")
        return 0
    else:
        print("⚠️  Certains tests ont échoué. Vérifiez vos modèles avant de pousser.")
        return 1


if __name__ == "__main__":
    exit(main()) 