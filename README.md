# Kerberos_project
This project aim to simulate the Kerberos Protocol and an alternative that eliminate the spof

---

# Kerberos Simulation Project

## Description
Ce projet est une simulation du protocole d'authentification Kerberos en Python. Il utilise Flask pour la création d'une interface web et Supabase pour la gestion des données d'authentification.

## Configuration de l'Environnement

### Prérequis
- Python 3.x
- pip (Gestionnaire de paquets Python)

### Création d'un Environnement Virtuel

Pour créer et activer un environnement virtuel, suivez ces étapes :

#### Sur Windows
```bash
# Création de l'environnement virtuel
python -m venv venv

# Activation de l'environnement virtuel
venv\Scripts\activate
```

#### Sur macOS et Linux
```bash
# Création de l'environnement virtuel
python3 -m venv venv

# Activation de l'environnement virtuel
source venv/bin/activate
```

### Installation des Dépendances

Après avoir activé l'environnement virtuel, installez les dépendances nécessaires avec la commande suivante :

```bash
pip install -r requirements.txt
```

## Fichier `requirements.txt`

Assurez-vous que votre fichier `requirements.txt` contient toutes les dépendances nécessaires :

```
flask
cryptography
supabase-py
```

## Lancement du Projet

Après l'installation des dépendances, lancez le projet avec :

```bash
python main.py
```



