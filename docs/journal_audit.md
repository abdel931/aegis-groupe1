\# Journal d'audit — Projet AEGIS

\## TechSud — BTC1 IPSSI



\---



\## 13/04/2026 — Lundi (Jour 1)



\### 09h00 — Réception du dossier de mission

\- Lecture du brief TechSud (Réf. TS-2026-SSI-001)

\- Incident détecté : vendredi 18 avril 2026 à 23h47

\- Serveur SRV-PROD-01 mis hors ligne à 00h23



\### 10h00 — Analyse des vecteurs d'attaque

\- 8 vecteurs identifiés (voir vecteurs\_attaque.md)

\- Hypothèse principale : intrusion via webshell (shell.php)

&#x20; uploadé sur formulaire de contact sans validation MIME

\- Persistance assurée via cron malveillant + C2 sur port 4444



\### 11h00 — Création de la VM de lab

\- Hyperviseur : VirtualBox

\- OS installé : Debian 12 (Bookworm)

\- Nom machine : techsud-server

\- Réseau : Host-Only (192.168.56.x) + NAT

\- SSH actif et fonctionnel



\### 12h00 — Initialisation du repo GitHub

\- Repo : https://github.com/abdel931/aegis-groupe1

\- Branche principale : main

\- Fichiers créés : README.md, docs/



\### À faire demain (Mardi)

\- \[ ] Créer utilisateur non-root (techsud-admin)

\- \[ ] SSH hardening : port 2222, no-root, clé uniquement

\- \[ ] Configurer réseau isolé

\- \[ ] Commit + push des modifications

