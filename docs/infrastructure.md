\# Infrastructure TechSud — Cartographie

\## Date : 13/04/2026



\## Réseau interne : 192.168.1.0/24

\## Passerelle : 192.168.1.1

\## DNS : 192.168.1.1

\## FAI : OVH Telecom — Fibre 500 Mb/s



| Nom | Rôle | OS | IP | État |

|-----|------|----|----|------|

| SRV-PROD-01 | Serveur principal (ERP + fichiers) | Debian 11 | 192.168.1.10 | ❌ HORS LIGNE |

| SRV-WEB-01 | Site vitrine + accès clients | Ubuntu 20.04 LTS | 192.168.1.20 | ✅ En ligne |

| SRV-BDD-01 | Base de données MariaDB 10.6 | Debian 11 | 192.168.1.30 | ✅ En ligne |

| FW-01 | Pare-feu périmétrique pfSense 2.6 | pfSense | 192.168.1.1 | ✅ En ligne |

| NAS-01 | Stockage / backups | Synology DSM 7 | 192.168.1.50 | ✅ En ligne |

| PC-ADM-01 | Poste admin DSI | Windows 11 Pro | 192.168.1.100 | ✅ En ligne |



\## Services exposés (à risque)



| Serveur | Service | Port | Exposition | Risque |

|---------|---------|------|------------|--------|

| SRV-PROD-01 | SSH | 22 | Internet | 🔴 CRITIQUE |

| SRV-WEB-01 | HTTP | 80 | Internet | 🟠 Élevé |

| SRV-WEB-01 | SSH root | 22 | Internet | 🔴 CRITIQUE |

| SRV-BDD-01 | MariaDB | 3306 | LAN+WAN? | 🔴 CRITIQUE |

