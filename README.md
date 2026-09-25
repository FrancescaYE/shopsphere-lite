☁️ ShopSphere Lite

ShopSphere Lite est une petite application e-commerce développée avec Python et Flask.

Ce projet fait partie de mon Cloud Engineering Journey et me sert de laboratoire pratique pour apprendre, déployer, dépanner et documenter progressivement une infrastructure Cloud sur Microsoft Azure.

🚀 Application en ligne

L’application est actuellement déployée sur Microsoft Azure App Service.

👉 Ouvrir ShopSphere Lite

L’application peut être consultée directement depuis le lien ci-dessus.

🎯 Objectif du projet

L’objectif de ce projet n’est pas uniquement de développer une application web, mais de l’utiliser comme base pratique pour développer mes compétences en Cloud Engineering.

L’infrastructure évoluera progressivement au fil de mon parcours Azure et couvrira notamment :

* Compute
* Networking
* Storage
* Bases de données
* Identité & Sécurité
* Gouvernance
* Gestion des coûts
* Monitoring
* Sauvegarde & Résilience
* Automatisation

🛠️ Technologies actuelles

* Python 3.12
* Flask
* SQLite
* HTML / CSS
* Microsoft Azure App Service
* Linux

  Architecture actuelle

ShopSphere Lite est actuellement déployé sur Azure App Service.

Architecture

                         INTERNET
                             │
                             ▼
                ┌────────────────────────┐
                │   Azure App Service    │
                │                        │
                │   Linux                │
                │   Python 3.12          │
                │   Flask                │
                │   Gunicorn             │
                └───────────┬────────────┘
                            │
                            ▼
                     SQLite Database

Composants Azure

Composant	Configuration
Service	Azure App Service
Type de publication	Code
Système d’exploitation	Linux
Runtime	Python 3.12
Région	South Africa North
Plan App Service	Free F1
Déploiement	ZIP Deployment
Serveur d’application	Gunicorn
Instances	1

Pourquoi Azure App Service ?

J’ai choisi Azure App Service pour cette première mise en pratique car ShopSphere Lite est une application web Python/Flask.

App Service fournit une plateforme PaaS, ce qui permet de me concentrer sur l’application et son déploiement sans avoir à administrer directement le système d’exploitation d’un serveur comme avec une Virtual Machine.

Cette approche correspond également aux objectifs du chapitre Azure Compute de mon parcours Cloud Engineering.



 Fonctionnalités

* Catalogue de produits
* Recherche de produits
* Détails d’un produit
* Ajout d’un produit
* Endpoint /health pour vérifier l’état de l’application

🚀 Déploiement Azure

ShopSphere Lite est déployé sur Azure App Service avec :

* Linux
* Python 3.12
* Région : South Africa North
* Plan : Free F1
* Déploiement : ZIP Deployment
* Serveur : Gunicorn
* 1 instance

Le déploiement a été réalisé depuis mon environnement Linux/WSL. Après le déploiement, j’ai vérifié les logs Azure, le démarrage de Gunicorn et le fonctionnement de l’application.

🔗 Application en ligne

Accéder à ShopSphere Lite

🧪 Tests réalisés

* Application accessible publiquement
* Catalogue fonctionnel
* Recherche fonctionnelle
* Consultation des produits
* Ajout de produit
* Endpoint /health
* Vérification des logs Azure
* Vérification du démarrage de Gunicorn
* Test depuis un appareil mobile

🔎 Troubleshooting

Pendant le déploiement et les tests, j’ai appliqué une démarche structurée :

Observe → Hypothèses → Vérifications → Interprétation → Diagnostic → Solution → Validation

Cette méthode m’a permis notamment de distinguer un problème lié à l’application d’un problème lié à l’infrastructure Azure.

📚 Ce que j’ai appris

Ce projet m’a permis de mettre en pratique :

* Azure Compute
* IaaS vs PaaS vs Serverless
* Azure Virtual Machines
* Azure App Service
* Scale Up / Scale Out
* Déploiement d’une application web
* Gunicorn
* Lecture des logs
* Vérification d’un service Cloud
* Git & GitHub
* Méthodologie de troubleshooting

⚠️ Limitation actuelle

L’application utilise actuellement SQLite comme base de données.

Cette solution est adaptée à cette étape d’apprentissage, mais elle n’est pas considérée comme une solution de base de données adaptée à une architecture de production.

L’architecture sera progressivement améliorée dans les prochains chapitres du parcours Cloud Engineering.

🔮 Évolution prévue

Le projet évoluera progressivement vers une architecture Azure plus complète avec notamment :

* Azure Networking
* Azure Storage
* Azure Database
* Identity & Security
* Governance
* Cost Management
* Monitoring
* Backup & Resilience
* Automation

L’objectif final est de transformer progressivement cette application en un projet Cloud Engineering complet, en documentant les choix d’architecture, les déploiements, les problèmes rencontrés et leurs solutions.

🎓 Cloud Engineering Journey

ShopSphere Lite est développé dans le cadre de ma préparation à la certification Microsoft AZ-900 et de mon parcours vers des rôles de Cloud Engineer / Azure Administrator / Cloud Operations Engineer / Infrastructure Engineer.
* Gunicorn
* Git / GitHub
