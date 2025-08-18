#!/usr/bin/env python3
"""
Test des migrations Alembic
Usage: python test_alembic.py
"""

import os
import subprocess
import sys

def test_alembic_migrations():
    """Teste les migrations Alembic"""
    print("🔄 Test des migrations Alembic...")
    
    try:
        # Vérifier que alembic est installé
        result = subprocess.run(
            ["alembic", "--version"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        print("✅ Alembic installé")
        
        # Vérifier la configuration
        result = subprocess.run(
            ["alembic", "show", "current"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        print("✅ Configuration Alembic valide")
        
        # Vérifier les migrations
        result = subprocess.run(
            ["alembic", "history"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        print("✅ Migrations disponibles")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur Alembic: {e}")
        print(f"Sortie: {e.stdout}")
        print(f"Erreur: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ Alembic non trouvé. Installez-le avec: pip install alembic")
        return False

if __name__ == "__main__":
    if test_alembic_migrations():
        print("🎉 Tests Alembic réussis!")
        sys.exit(0)
    else:
        print("⚠️  Tests Alembic échoués!")
        sys.exit(1) 