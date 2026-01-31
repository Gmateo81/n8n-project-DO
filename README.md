# Serveur MCP de Scoring de Villes & Workflow n8n 🌍

Ce projet permet de scorer des villes pour la recherche de stages et d'automatiser le processus via n8n.

## 📦 Fichiers Essentiels

Pour installer ce projet sur une nouvelle machine, vous avez besoin de ces 4 fichiers :

1.  `mcp_server.py` : Le serveur MCP (Python).
2.  `city_data.json` : La base de données des scores des villes.
3.  `run_mcp.sh` : Le script pour lancer le serveur.
4.  `requirements.txt` : La liste des dépendances Python.


## Installation & Lancement

Suivez ces étapes pour démarrer le projet :

### 1. Installer les dépendances

Il est recommandé d'utiliser un environnement virtuel Python :

```bash
# Création de l'environnement virtuel
python3 -m venv .venv

# Activation
source .venv/bin/activate

# Installation des paquets requis
pip install -r requirements.txt
```

### 2. Démarrer le Serveur MCP

Lancez simplement le script fourni :

```bash
chmod +x run_mcp.sh  # Rendre le script exécutable si besoin
./run_mcp.sh
```

Le serveur écoutera sur le port configuré (par défaut 8000).
