# CI-CD-pipeline
## Objectif

Créer un pipeline CI/CD pour automatiser le déploiement et les tests d’une application .

## Étapes principales du pipeline
1) Build / Installation des dépendances

Installer Python et les packages requis via requirements.txt.

2)Test

Lancer les tests unitaires définis dans tests/test_app.py avec pytest.

3)Déploiement 

Si tous les tests passent, l’application peut être déployée automatiquement sur une plateforme cible (Docker).

## Technologies utilisées

- **Flask** : Framework web léger pour Python.
- **pytest** : Framework de tests unitaires pour Python.
- **GitHub Actions** : Plateforme d'automatisation des workflows CI/CD.


## Fonctionnement du workflow GitHub Actions
Le pipeline s’exécute à chaque push ou pull_request sur la branche main.

Jobs :

Setup Python : Installation de la version de Python définie dans le workflow.

Install Dependencies : Installation des packages nécessaires (Flask, pytest).

Run Tests : Exécution des tests unitaires pour valider l’application.


