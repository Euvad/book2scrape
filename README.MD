# BookToScrape - Scraping de données du site "https://books.toscrape.com/"

Ce projet consiste en un script de scraping qui permet de récupérer diverses données à partir du site "https://books.toscrape.com/". Le script parcourt les différentes pages du site pour extraire des informations telles que les prix, les descriptions, les titres, les notations, les images avec leurs fichiers, les liens vers les livres, et bien d'autres encore.

## Fonctionnalités

- Récupération des données : Le script est capable de naviguer à travers les différentes catégories et pages du site "https://books.toscrape.com/" pour extraire des informations détaillées sur chaque livre.
- Informations complètes : Il récupère des données essentielles telles que les prix, les descriptions, les titres, les notations, les images (avec leurs fichiers) et les liens vers les livres correspondants.
- Structure organisée : Les données sont organisées de manière structurée, permettant ainsi une utilisation facile et une analyse ultérieure.
- Personnalisable : Le script est facilement adaptable pour récupérer des informations supplémentaires en fonction des besoins spécifiques de l'utilisateur.

## Utilisation

1. Cloner le dépôt : `git clone https://github.com/HelloVad/book2scrape.git`
2. Accéder au répertoire du projet : `cd BookToScrape`
3. Créer un environnement virtuel (venv) pour isoler les dépendances du projet : `python -m venv venv`
4. Activer l'environnement virtuel :
   - Sur Windows : `venv\Scripts\activate`
   - Sur macOS et Linux : `source venv/bin/activate`
5. Installer les dépendances requises : `pip install -r requirements.txt`
6. Exécuter le script : `python scrape.py`
7. Les données seront extraites et enregistrées dans des fichiers de sortie au format CSV.

N'hésitez pas à explorer les options disponibles dans le script pour personnaliser les informations que vous souhaitez extraire du site.

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, veuillez ouvrir une pull request avec vos modifications. Assurez-vous de respecter les meilleures pratiques de codage et d'ajouter des tests appropriés le cas échéant.

## Remarque

Ce script de scraping a été développé dans un but éducatif et pour des fins non commerciales. Veuillez utiliser ce script de manière responsable et respectez les politiques du site "https://books.toscrape.com/" en matière de scraping.

**Avertissement :** Scraping de sites Web sans autorisation préalable peut violer les conditions d'utilisation du site ciblé. Veuillez utiliser ce script à vos propres risques.

## Auteur

Ce projet a été développé par [HelloVad](https://github.com/HelloVad). N'hésitez pas à me contacter si vous avez des questions ou des suggestions liées à ce projet.