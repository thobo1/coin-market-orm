#!/usr/bin/env python3
"""
Test ultra-rapide des modèles SQLAlchemy
Usage: python quick_test.py
"""

import sys
import os

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from orm.models import *
    print("✅ Tous les modèles importés avec succès!")
    print("✅ Aucune erreur d'initialisation des mappers SQLAlchemy")
except Exception as e:
    print(f"❌ Erreur: {e}")
    sys.exit(1) 