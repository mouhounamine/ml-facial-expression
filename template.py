# IGNOREZ CE FICHIER

import os

def create_project_structure():
    # Définition de la structure du projet
    project_structure = {
        "src": [
            "data/train/",  # Dossier pour les données d'entraînement
            "data/test/",   # Dossier pour les données de test
            "models/",      # Dossier pour stocker les modèles
            "utils/",       # Dossier pour les fonctions utilitaires
            "checkpoints/", # Dossier pour sauvegarder les modèles entraînés
            "train.py",     # Script principal d'entraînement
            "test.py",      # Script pour tester le modèle
            "predict.py",   # Script pour faire des prédictions sur une image
            "config.py",    # Fichier de configuration des hyperparamètres
            "README.md"     # Documentation du projet
        ],
        "src/models": [
            "resemotenet.py"  # Contient l'architecture du modèle ResEmoteNet
        ],
        "src/utils": [
            "dataloader.py"  # Fonctions pour charger les données et appliquer les transformations
        ]
    }

    # Création des dossiers et fichiers
    for root, paths in project_structure.items():
        for path in paths:
            full_path = os.path.join(root, path)
            if path.endswith("/"):  # Dossier
                os.makedirs(full_path, exist_ok=True)
            else:  # Fichier
                with open(full_path, "w") as f:
                    if path == "train.py":
                        f.write("""\
# train.py : Ce script gère l'entraînement du modèle.
# Il charge les données, entraîne ResEmoteNet et enregistre le modèle entraîné.
                        """)
                    elif path == "test.py":
                        f.write("""\
# test.py : Ce script charge un modèle entraîné et évalue sa performance sur les données de test.
                        """)
                    elif path == "predict.py":
                        f.write("""\
# predict.py : Ce script utilise un modèle entraîné pour prédire l'émotion sur une image donnée.
                        """)
                    elif path == "config.py":
                        f.write("""\
# config.py : Contient les hyperparamètres et configurations du projet.
                        """)
                    elif path == "README.md":
                        f.write("""\
# EmotionRecognition

Projet de reconnaissance des émotions faciales basé sur ResEmoteNet et PyTorch.
                        """)
                    elif path == "models/resemotenet.py":
                        f.write("""\
# resemotenet.py : Contient l'architecture du modèle ResEmoteNet utilisé pour la reconnaissance des émotions faciales.
                        """)
                    elif path == "utils/dataloader.py":
                        f.write("""\
# dataloader.py : Ce fichier contient les fonctions pour charger les images avec les transformations appropriées.
                        """)

    print("Structure du projet créée avec succès !")

# Exécuter la création du projet
create_project_structure()
