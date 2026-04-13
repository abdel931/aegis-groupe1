\# Vecteurs d'attaque identifiés — TechSud

\## Date d'analyse : 13/04/2026

\## Analyste : \[Ton prénom]



\---



\## VA-01 — Webshell via upload sans validation MIME

\- \*\*Fichier\*\* : /var/www/html/upload/shell.php

\- \*\*Cause\*\* : Formulaire de contact sans vérification du type de fichier

\- \*\*Impact\*\* : Exécution de code arbitraire sur SRV-WEB-01

\- \*\*Criticité\*\* : 🔴 CRITIQUE



\## VA-02 — SSH exposé sur Internet avec accès root

\- \*\*Serveurs concernés\*\* : SRV-PROD-01 (port 22), SRV-WEB-01 (port 22)

\- \*\*Cause\*\* : PermitRootLogin yes + mots de passe faibles (ex: prenom2024)

\- \*\*Impact\*\* : Prise de contrôle totale du serveur

\- \*\*Criticité\*\* : 🔴 CRITIQUE



\## VA-03 — Compte de déploiement réactivé (deploy)

\- \*\*Connexion SSH\*\* depuis 185.220.101.47 (Tor exit node)

\- \*\*Durée\*\* : 1h47min — compte normalement désactivé

\- \*\*Impact\*\* : Accès persistant à l'insu de l'administrateur

\- \*\*Criticité\*\* : 🔴 CRITIQUE



\## VA-04 — Processus C2 (Command \& Control)

\- \*\*Processus\*\* : kworker/u4:2 (PID 4821) — déguisé en processus kernel

\- \*\*Connexion sortante\*\* : 45.142.212.100:4444

\- \*\*Cron malveillant\*\* : /etc/cron.d/sysupdate — exécute sshd\_bak toutes les 5 min

\- \*\*Impact\*\* : Persistance + exfiltration de données

\- \*\*Criticité\*\* : 🔴 CRITIQUE



\## VA-05 — Base de données MariaDB potentiellement exposée sur WAN

\- \*\*Port\*\* : 3306 — configuration pare-feu inconnue

\- \*\*Cause\*\* : Règles pfSense non documentées, jamais révisées

\- \*\*Impact\*\* : Accès direct à toutes les données clients

\- \*\*Criticité\*\* : 🟠 ÉLEVÉE



\## VA-06 — Logs partiellement effacés

\- \*\*Fichier\*\* : /var/log/auth.log

\- \*\*Période manquante\*\* : 17/04 08h00 → 18/04 21h00

\- \*\*Impact\*\* : Impossibilité de retracer l'intrusion complète

\- \*\*Criticité\*\* : 🟠 ÉLEVÉE



\## VA-07 — Absence de HTTPS sur site vitrine

\- \*\*Serveur\*\* : SRV-WEB-01 — HTTP port 80 uniquement

\- \*\*Impact\*\* : Données transmises en clair, possibilité MITM

\- \*\*Criticité\*\* : 🟠 ÉLEVÉE



\## VA-08 — Sauvegardes non testées + pas de backup hors-site

\- \*\*NAS-01\*\* : backups hebdomadaires non vérifiés depuis 3 mois

\- \*\*Impact\*\* : Aucune garantie de restauration en cas de ransomware

\- \*\*Criticité\*\* : 🟠 ÉLEVÉE

