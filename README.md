# ShopSphere Lite

ShopSphere Lite est une petite application e-commerce développée avec Python et Flask.

Ce projet fait partie de mon Cloud Engineering Journey et sert de laboratoire pratique pour apprendre à concevoir, déployer, sécuriser, dépanner et documenter progressivement une infrastructure Cloud sur Microsoft Azure.

L’objectif n’est pas uniquement de développer une application web, mais de faire évoluer progressivement son infrastructure afin de mettre en pratique les concepts du Cloud Engineering.

---

## Objectif du projet

ShopSphere Lite évolue progressivement au fil de mon parcours Azure. Les prochaines étapes du projet couvriront notamment :

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

---

## Technologies actuelles

* *Langage & Framework :* Python 3.12, Flask
* *Serveur WSGI :* Gunicorn
* *Base de données :* SQLite
* *Frontend :* HTML / CSS
* *OS :* Ubuntu Linux
* *Cloud :* Microsoft Azure
* *Outils :* Git / GitHub

---

## Infrastructure Azure actuelle

* *Resource Group :* ShopSphere-Lite
* *Virtual Network :* ShopSphere-Lite-VNet (Address space : 10.0.0.0/16)
* *Subnet :* subnet-web (Address space : 10.0.1.0/24)
* *Virtual Machine :* ShopShere-Lite-VM (OS : Ubuntu Server 24.04 LTS, Size : Standard_B2als_v2, Availability Zone : Zone 1)
* *Networking :* Public IP (ShopShere-Lite-VM-ip), NSG (ShopSphere-Lite-VM-NSG), port applicatif : 8000

---

## Architecture actuelle

*Internet*

⬇️

*Public IP*

⬇️

*Network Security Group*

⬇️

*TCP 8000*

⬇️

*Azure Linux VM*

⬇️

*Gunicorn :8000*

⬇️

*Flask*

⬇️

*SQLite*

> *Note :* Gunicorn est directement exposé sur le port 8000 dans cette version de laboratoire. Nginx n’est pas utilisé dans ShopSphere Lite (une configuration avec Nginx a été utilisée séparément dans le projet autonome GreenCart).

---

## Networking and Security

La VM est intégrée dans un réseau virtuel Azure dédié. Le Network Security Group (NSG) contrôle les communications réseau autorisées. Les principaux concepts mis en pratique sont :

* IPv4 & CIDR
* Virtual Network & Subnet
* Public IP & Private IP
* Network Security Groups (Inbound / Outbound rules, Rule priorities)
* SSH & Application ports

> L’accès administratif à la VM s’effectue via SSH avec une clé privée. Les clés privées ne sont jamais stockées dans le repository GitHub.

---

## Déploiement de l’application

L’application Flask est exécutée sur la VM Linux avec Gunicorn.

*Flask application*

⬇️

*Gunicorn*

⬇️

*TCP :8000*

⬇️

*Azure NSG*

⬇️

*Public IP*

Le déploiement comprend notamment :

1. Installation de Python
2. Création d’un environnement virtuel
3. Installation des dépendances
4. Configuration de l’application
5. Lancement avec Gunicorn
6. Configuration du réseau Azure et ouverture du port applicatif nécessaire
7. Tests locaux et depuis Internet

---

## Tests réalisés

Les tests effectués comprennent notamment :

* Démarrage de la VM et connexion SSH
* Vérification de l’adresse IP privée et de la connectivité réseau sortante
* Vérification du port d’écoute
* Lancement de l’application avec Gunicorn
* Test local de l’application et accès depuis Internet
* Vérification du fonctionnement de Flask et de l’endpoint /health

---

## Troubleshooting

Une démarche structurée est utilisée lors des problèmes :

*Observe*

⬇️

*Hypothèses*

⬇️

*Vérifications*

⬇️

*Interprétation*

⬇️

*Diagnostic*

⬇️

*Solution*

⬇️

*Validation*

Pour les problèmes de connectivité, le raisonnement suit le chemin suivant :

*DNS*

⬇️

*Endpoint / IP*

⬇️

*Routing*

⬇️

*NSG*

⬇️

*OS Firewall*

⬇️

*Port / Protocol*

⬇️

*Service / Listener*

⬇️

*Application*

Cette méthode permet de distinguer progressivement un problème lié au DNS, au réseau Azure, au NSG, à Linux, au Firewall, au Port, au Service ou à l’Application.

---

## Ce que j’ai appris

Ce projet m’a permis de mettre en pratique :

* Azure Virtual Machines & Azure Networking (VNets, Subnets, Public/Private IPs, NSGs)
* SSH & Linux Administration
* Python, Flask & Gunicorn
* Web application deployment
* Git & GitHub
* Network & Layer-based troubleshooting

---

## Limitation actuelle

L’application utilise actuellement SQLite et fonctionne sur une seule Virtual Machine. Cette architecture est destinée à l’apprentissage et à la mise en pratique des concepts Cloud, et n’est pas présentée comme une architecture de production complète. L’infrastructure sera progressivement améliorée au fil du Cloud Engineering Journey.

---

## Évolution prévue

ShopSphere Lite évoluera progressivement vers une architecture Azure plus complète. Les prochaines évolutions pourront notamment inclure :

* Azure Storage & Azure Database
* Identity and Security
* Governance & Cost Management
* Monitoring
* Backup and Resilience
* Automation

Les choix d’architecture seront documentés au fur et à mesure de l’évolution du projet.

---

## Cloud Engineering Journey

ShopSphere Lite est développé dans le cadre de mon Cloud Engineering Journey. Le parcours est principalement orienté vers :

* Microsoft Azure (AZ-900, AZ-104)
* Cloud Engineering & Azure Administration
* Cloud Operations & Infrastructure Engineering

L’objectif est de construire progressivement une infrastructure Cloud complète tout en développant mes compétences en déploiement, réseau, sécurité, supervision, automatisation et troubleshooting.

---

*Auteur :* Francesca
Cloud Engineering Journey — Azure
