ShopSphere Lite

ShopSphere Lite est une petite application e-commerce développée avec Python et Flask.

Ce projet fait partie de mon Cloud Engineering Journey et sert de laboratoire pratique pour apprendre à concevoir, déployer, sécuriser, dépanner et documenter progressivement une infrastructure Cloud sur Microsoft Azure.

L’objectif n’est pas uniquement de développer une application web, mais de faire évoluer progressivement son infrastructure afin de mettre en pratique les concepts du Cloud Engineering.

Objectif du projet

ShopSphere Lite évolue progressivement au fil de mon parcours Azure.

Les prochaines étapes du projet couvriront notamment :

* Compute
* Networking
* Storage
* Databases
* Identity & Security
* Governance
* Cost Management
* Monitoring
* Backup & Resilience
* Automation

Technologies actuelles

* Python 3.12
* Flask
* Gunicorn
* SQLite
* HTML / CSS
* Ubuntu Linux
* Microsoft Azure
* Git / GitHub

Infrastructure Azure actuelle

ShopSphere Lite est actuellement déployé sur une Azure Linux Virtual Machine.

Architecture actuelle

Internet
   |
   v
Public IP
   |
   v
Network Security Group
   |
   | TCP 8000
   v
Azure Linux VM
   |
   v
Gunicorn :8000
   |
   v
Flask
   |
   v
SQLite

Le trafic web de test suit donc le chemin suivant :

Internet
    |
    v
Public IP
    |
    v
NSG
    |
    v
TCP 8000
    |
    v
Gunicorn
    |
    v
Flask
    |
    v
SQLite

Gunicorn est directement exposé sur le port 8000 dans cette version de laboratoire.

Nginx n’est pas utilisé dans ShopSphere Lite.

Une configuration avec Nginx a été utilisée séparément dans le projet autonome GreenCart.

Configuration Azure

Resource Group

ShopSphere-Lite

Virtual Network

Name: ShopSphere-Lite-VNet
Address space: 10.0.0.0/16

Subnet

Name: subnet-web
Address space: 10.0.1.0/24

Virtual Machine

Name: ShopShere-Lite-VM
OS: Ubuntu Server 24.04 LTS
Size: Standard_B2als_v2
Availability Zone: Zone 1

Networking

Public IP: ShopShere-Lite-VM-ip
NSG: ShopSphere-Lite-VM-NSG
Application port: 8000

Application

Application server: Gunicorn
Framework: Flask
Database: SQLite

Networking and Security

La VM est intégrée dans un réseau virtuel Azure dédié.

Le Network Security Group (NSG) contrôle les communications réseau autorisées.

Les principaux concepts mis en pratique sont :

* IPv4
* CIDR
* Virtual Network
* Subnet
* Public IP
* Private IP
* Network Security Groups
* Inbound rules
* Outbound rules
* Rule priorities
* SSH
* Application ports

L’accès administratif à la VM s’effectue via SSH avec une clé privée.

Les clés privées ne sont jamais stockées dans le repository GitHub.

Déploiement de l’application

L’application Flask est exécutée sur la VM Linux avec Gunicorn.

Le principe de fonctionnement est :

Flask application
       |
       v
    Gunicorn
       |
       v
   TCP :8000
       |
       v
   Azure NSG
       |
       v
   Public IP

Le déploiement comprend notamment :

* Installation de Python
* Création d’un environnement virtuel
* Installation des dépendances
* Configuration de l’application
* Lancement avec Gunicorn
* Configuration du réseau Azure
* Ouverture du port applicatif nécessaire
* Tests locaux
* Tests depuis Internet

Tests réalisés

Les tests effectués comprennent notamment :

* Démarrage de la VM
* Connexion SSH
* Vérification de l’adresse IP privée
* Vérification de la connectivité réseau sortante
* Vérification du port d’écoute
* Lancement de l’application avec Gunicorn
* Test local de l’application
* Test d’accès depuis Internet
* Vérification du fonctionnement de Flask
* Vérification de l’endpoint /health

Troubleshooting

Une démarche structurée est utilisée lors des problèmes :

Observe
   |
   v
Hypothèses
   |
   v
Vérifications
   |
   v
Interprétation
   |
   v
Diagnostic
   |
   v
Solution
   |
   v
Validation

Pour les problèmes de connectivité, le raisonnement suit notamment le chemin suivant :

DNS
 |
 v
Endpoint / IP
 |
 v
Routing
 |
 v
NSG
 |
 v
OS Firewall
 |
 v
Port / Protocol
 |
 v
Service / Listener
 |
 v
Application

Cette méthode permet de distinguer progressivement un problème lié à :

* DNS
* Azure Networking
* NSG
* Linux
* Firewall
* Port
* Service
* Application

Ce que j’ai appris

Ce projet m’a permis de mettre en pratique :

* Azure Virtual Machines
* Azure Networking
* Virtual Networks
* Subnets
* Public and Private IP addresses
* Network Security Groups
* SSH
* Linux
* Python
* Flask
* Gunicorn
* Web application deployment
* Git
* GitHub
* Network troubleshooting
* Layer-based troubleshooting

Limitation actuelle

L’application utilise actuellement SQLite et fonctionne sur une seule Virtual Machine.

Cette architecture est destinée à l’apprentissage et à la mise en pratique des concepts Cloud.

Elle n’est pas présentée comme une architecture de production complète.

L’infrastructure sera progressivement améliorée au fil du Cloud Engineering Journey.

Évolution prévue

ShopSphere Lite évoluera progressivement vers une architecture Azure plus complète.

Les prochaines évolutions pourront notamment inclure :

* Azure Storage
* Azure Database
* Identity and Security
* Governance
* Cost Management
* Monitoring
* Backup and Resilience
* Automation

Les choix d’architecture seront documentés au fur et à mesure de l’évolution du projet.

Cloud Engineering Journey

ShopSphere Lite est développé dans le cadre de mon Cloud Engineering Journey.

Le parcours est principalement orienté vers :

* Microsoft Azure
* AZ-900
* AZ-104
* Cloud Engineering
* Azure Administration
* Cloud Operations
* Infrastructure Engineering

L’objectif est de construire progressivement une infrastructure Cloud complète tout en développant mes compétences en déploiement, réseau, sécurité, supervision, automatisation et troubleshooting.

Author

Francesca

Cloud Engineering Journey — Azure
