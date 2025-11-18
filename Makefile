# Makefile pour les tests des modèles SQLAlchemy

.PHONY: test test-quick test-full install-hook clean

# Test rapide (recommandé pour le développement)
test-quick:
	@echo "🔍 Test rapide des modèles..."
	@python3 quick_test.py

# Test complet (pour validation complète)
test-full:
	@echo "🔍 Test complet des modèles..."
	@python3 test_models.py

# Test par défaut
test: test-quick

# Installer le hook de pre-commit
install-hook:
	@echo "📦 Installation du hook de pre-commit..."
	@cp pre-commit-hook.sh .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo "✅ Hook installé!"

# Nettoyer les fichiers de test
clean:
	@echo "🧹 Nettoyage..."
	@rm -f *.pyc
	@rm -f __pycache__/
	@echo "✅ Nettoyage terminé!"

# Aide
help:
	@echo "Commandes disponibles:"
	@echo "  make test-quick    - Test rapide des modèles (recommandé)"
	@echo "  make test-full     - Test complet des modèles"
	@echo "  make test          - Test rapide (par défaut)"
	@echo "  make install-hook  - Installer le hook de pre-commit"
	@echo "  make clean         - Nettoyer les fichiers temporaires"
	@echo "  make help          - Afficher cette aide" 