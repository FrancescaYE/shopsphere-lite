☁️ ShopSphere Lite

ShopSphere Lite est une petite application e-commerce développée en Python avec Flask et utilisant SQLite comme base de données.

Cette application fait partie de ma Cloud Engineering Journey et me sert de projet pratique pour appliquer progressivement les concepts d’infrastructure et de services Cloud sur Microsoft Azure.

🎯 Objectif

L’objectif de ShopSphere Lite n’est pas de construire une plateforme e-commerce complète, mais de disposer d’une application simple que je peux faire évoluer au fur et à mesure de mon apprentissage du Cloud.

Le projet me permet notamment de pratiquer :

* le déploiement d’applications sur Azure ;
* Azure Compute ;
* Azure App Service ;
* la compréhension des modèles IaaS et PaaS ;
* le scaling ;
* la lecture et l’interprétation des logs ;
* le troubleshooting ;
* puis progressivement le réseau, le stockage, les bases de données, la sécurité, le monitoring et l’automatisation.

🏗️ Architecture actuelle

                    Internet
                       │
                       ▼
             ┌──────────────────┐
             │   Azure App      │
             │     Service      │
             │                  │
             │  Python / Flask  │
             └────────┬─────────┘
                      │
                      ▼
                 ┌─────────┐
                 │ SQLite  │
                 └─────────┘

Cette architecture représente l’état actuel du projet dans le cadre de mon apprentissage. Elle sera progressivement améliorée au cours de ma Cloud Engineering Journey.

🛠️ Technologies

Application

* Python 3.12
* Flask
* SQLite
* HTML / CSS

Cloud

* Microsoft Azure
* Azure App Service
* Linux App Service
* Gunicorn
* ZIP Deployment

✨ Fonctionnalités

ShopSphere Lite permet actuellement de :

* consulter un catalogue de produits ;
* rechercher des produits ;
* consulter les détails d’un produit ;
* ajouter un produit ;
* vérifier l’état de l’application avec un endpoint /health.

🚀 Déploiement Azure

L’application est actuellement hébergée sur Azure App Service.

Configuration utilisée

* Service: Azure App Service
* OS: Linux
* Runtime: Python 3.12
* Region: South Africa North
* Pricing tier: Free F1
* Deployment: ZIP Deployment
* Application server: Gunicorn

Pourquoi Azure App Service ?

App Service a été choisi parce que ShopSphere Lite est une application web Python/Flask et que l’objectif du projet est de limiter l’administration de l’infrastructure.

Azure App Service est une solution PaaS : Azure prend en charge une grande partie de l’infrastructure et de la plateforme sous-jacente, ce qui permet de se concentrer davantage sur l’application.

Par rapport à une Virtual Machine, je n’ai donc pas besoin d’administrer directement le système d’exploitation de la même manière.

🧪 Tests et validation

Après le déploiement, plusieurs vérifications ont été réalisées :

* accès à l’application depuis Internet ;
* affichage du catalogue ;
* recherche de produits ;
* consultation des détails d’un produit ;
* test de l’endpoint /health ;
* vérification des logs Azure ;
* vérification du démarrage de Gunicorn ;
* test depuis un appareil mobile.

Health check

GET /health

Réponse attendue :

{
  "status": "ok"
}

🔎 Troubleshooting

Une partie importante du projet consiste à développer une méthode de troubleshooting plutôt qu’à appliquer des commandes sans comprendre leur objectif.

La méthode utilisée est :

Observe
   ↓
Formulate hypotheses
   ↓
Perform checks
   ↓
Interpret results
   ↓
Diagnose
   ↓
Apply a solution
   ↓
Validate

Lors du déploiement, les logs Azure ont notamment permis de vérifier :

* la version de Python utilisée ;
* la détection de Flask ;
* la génération de la commande Gunicorn ;
* le démarrage des workers ;
* l’écoute de l’application sur le port fourni par Azure.

📚 Ce que j’ai appris

À travers ce projet, j’ai consolidé plusieurs concepts de Cloud Engineering :

Azure Compute

* rôle du Compute dans le Cloud ;
* Azure Virtual Machines ;
* Virtual Machine Scale Sets ;
* Azure App Service ;
* Containers ;
* Azure Functions ;
* choix d’un modèle Compute selon le workload.

Scaling

* Scale Up / Scale Down ;
* Scale Out / Scale In ;
* différence entre augmenter les ressources d’une instance et augmenter le nombre d’instances ;
* relation entre scaling et résilience.

Azure App Service

* création d’une Web App ;
* configuration d’un runtime Python ;
* déploiement d’une application Flask ;
* ZIP Deployment ;
* lecture des logs ;
* compréhension du démarrage avec Gunicorn.

Troubleshooting

J’ai également commencé à appliquer une démarche structurée :

Observer → formuler des hypothèses → vérifier → interpréter → diagnostiquer → corriger → valider.

⚠️ Limites actuelles

ShopSphere Lite est avant tout un projet d’apprentissage Cloud.

La base de données actuelle utilise SQLite. Cette architecture est volontairement simple pour les premières étapes du projet et sera étudiée et améliorée dans les prochains chapitres.

Le projet ne doit donc pas être considéré comme une architecture e-commerce production-ready.

🔮 Prochaines évolutions

L’architecture de ShopSphere Lite évoluera progressivement avec ma formation :

* [ ]	Azure Networking
* [ ]	Azure Storage
* [ ]	Azure Database
* [ ]	Identity & Security
* [ ]	Governance
* [ ]	Cost Management
* [ ]	Monitoring
* [ ]	Backup & Resilience
* [ ]	Troubleshooting avancé
* [ ]	Azure CLI / Automation
* [ ]	Architecture Cloud finale

L’objectif est de transformer progressivement cette petite application en un laboratoire Cloud complet permettant de mettre en pratique les compétences acquises tout au long de ma formation.

🎓 Cloud Engineering Journey

ShopSphere Lite est développé dans le cadre de ma préparation à la certification Microsoft AZ-900 et de mon parcours vers les métiers de :

* Cloud Engineer
* Azure Administrator
* Cloud Operations Engineer
* Infrastructure Engineer

Ce repository documente mon apprentissage, mes expérimentations, mes erreurs, mes corrections et l’évolution progressive de l’architecture.

⸻

Learning in public • Building step by step • Cloud Engineering Journey 
