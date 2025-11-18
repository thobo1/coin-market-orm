# Tests des Modèles SQLAlchemy

Ce document explique comment tester vos modèles SQLAlchemy avant de pousser sur GitLab.

## 🚀 Tests Rapides

### Test Ultra-Rapide (Recommandé)
```bash
python3 quick_test.py
```
ou
```bash
make test-quick
```

Ce test vérifie uniquement que tous les modèles peuvent être importés sans erreur d'initialisation des mappers SQLAlchemy.

### Test Complet
```bash
python3 test_models.py
```
ou
```bash
make test-full
```

Ce test vérifie :
- ✅ Import de tous les modèles
- ✅ Création des tables en base de données
- ✅ Test des relations entre les modèles

## 🔧 Installation du Hook Pre-Commit

Pour automatiser les tests avant chaque commit :

```bash
make install-hook
```

Cela installera un hook Git qui exécutera automatiquement le test rapide avant chaque commit.

## 📋 Commandes Utiles

```bash
# Test rapide (par défaut)
make test

# Test complet
make test-full

# Installer le hook pre-commit
make install-hook

# Nettoyer les fichiers temporaires
make clean

# Afficher l'aide
make help
```

## 🐛 Résolution des Problèmes

### Erreur "AmbiguousForeignKeysError"
Si vous obtenez cette erreur, cela signifie qu'il y a plusieurs chemins de clés étrangères entre deux tables. Solution :

1. Spécifiez explicitement la clé étrangère dans la relation :
```python
relationship("Model", foreign_keys="[Model.foreign_key_column]")
```

2. Ou utilisez `primaryjoin` :
```python
relationship("Model", primaryjoin="Parent.id == Child.parent_id")
```

### Erreur "Invalid keyword argument"
Vérifiez que les champs utilisés dans les tests correspondent aux colonnes définies dans vos modèles.

## 📝 Exemples d'Erreurs Courantes

### ❌ Avant (Problématique)
```python
# Dans Conversation
messages = relationship("Message", back_populates="conversation")

# Dans Message  
conversation = relationship("Conversation", back_populates="messages")
```

### ✅ Après (Corrigé)
```python
# Dans Conversation
messages = relationship("Message", primaryjoin="Conversation.id == Message.conversation_id", back_populates="conversation")

# Dans Message
conversation = relationship("Conversation", foreign_keys=[conversation_id], back_populates="messages")
```

## 🎯 Workflow Recommandé

1. **Développement** : Utilisez `make test-quick` après chaque modification de modèle
2. **Avant commit** : Le hook pre-commit s'exécutera automatiquement
3. **Validation complète** : Utilisez `make test-full` avant de pousser sur GitLab

## 📊 Interprétation des Résultats

- **✅ Tous les tests passent** : Vos modèles sont prêts pour GitLab
- **⚠️ Certains tests échouent** : Corrigez les erreurs avant de pousser
- **❌ Erreur critique** : Vérifiez la syntaxe de vos modèles 