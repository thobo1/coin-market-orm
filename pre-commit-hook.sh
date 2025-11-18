#!/bin/bash
"""
Script de pre-commit hook pour tester les modèles SQLAlchemy
Placez ce fichier dans .git/hooks/pre-commit et rendez-le exécutable
"""

echo "🔍 Test des modèles SQLAlchemy avant commit..."

# Test rapide des modèles
if ! python3 quick_test.py; then
    echo "❌ Test rapide échoué. Commit annulé."
    exit 1
fi

echo "✅ Test rapide réussi!"

# Test complet (optionnel - décommentez si vous voulez des tests plus complets)
# if ! python3 test_models.py; then
#     echo "❌ Test complet échoué. Commit annulé."
#     exit 1
# fi

echo "🎉 Tous les tests sont passés. Commit autorisé."
exit 0 