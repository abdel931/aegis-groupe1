import socket
import json
import csv
import datetime
import os
import subprocess
import platform

# ─────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────

CIBLE = "127.0.0.1"

PORTS_A_SCANNER = [21, 22, 23, 25, 80, 443, 445, 3306, 3389, 5001, 8080]

NOMS_PORTS = {
    21:   "FTP",
    22:   "SSH",
    23:   "Telnet",
    25:   "SMTP",
    80:   "HTTP",
    443:  "HTTPS",
    445:  "SMB",
    3306: "MariaDB",
    3389: "RDP",
    5001: "Synology DSM",
    8080: "HTTP alternatif"
}

FICHIERS_SUSPECTS = [
    "/tmp/.x11-unix/sshd_bak",
    "/etc/cron.d/sysupdate",
    "/var/www/html/upload/shell.php",
    "test_malware.txt"  # pour simulation
]

PROCESSUS_SUSPECTS = ["kworker", "nc", "bash", "sh"]

# ─────────────────────────────────────────
# SCAN PORTS
# ─────────────────────────────────────────

def scanner_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        resultat = sock.connect_ex((ip, port))
        sock.close()
        return "OUVERT ⚠️" if resultat == 0 else "fermé"
    except:
        return "erreur"

def analyser_risque(port, statut):
    if statut != "OUVERT ⚠️":
        return "—"

    risques = {
        21: "CRITIQUE — FTP en clair",
        22: "ÉLEVÉ — SSH exposé",
        23: "CRITIQUE — Telnet",
        25: "MOYEN — SMTP",
        80: "ÉLEVÉ — HTTP",
        443: "OK — HTTPS",
        445: "CRITIQUE — SMB exposé",
        3306: "CRITIQUE — BDD exposée",
        3389: "ÉLEVÉ — RDP",
        5001: "MOYEN — Synology",
        8080: "MOYEN — HTTP alternatif"
    }
    return risques.get(port, "INCONNU")

def lancer_audit(ip):
    print(f"\n{'='*60}")
    print("  🛡️ AUDIT AEGIS — TechSud")
    print(f"  Cible : {ip}")
    print(f"  Date  : {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'='*60}\n")

    resultats = []

    for port in PORTS_A_SCANNER:
        service = NOMS_PORTS.get(port, "Inconnu")
        statut = scanner_port(ip, port)
        risque = analyser_risque(port, statut)

        print(f"  Port {port:5} | {service:15} | {statut:12} | {risque}")

        resultats.append({
            "port": port,
            "service": service,
            "statut": statut,
            "risque": risque
        })

    return resultats

# ─────────────────────────────────────────
# EXPORT
# ─────────────────────────────────────────

def exporter_json(resultats):
    with open("rapport_audit.json", "w", encoding="utf-8") as f:
        json.dump(resultats, f, indent=4, ensure_ascii=False)
    print("\n✅ Rapport JSON généré")

def exporter_csv(resultats):
    with open("rapport_audit.csv", "w", newline="", encoding="utf-8") as f:
        champs = ["port", "service", "statut", "risque"]
        writer = csv.DictWriter(f, fieldnames=champs)
        writer.writeheader()
        writer.writerows(resultats)
    print("✅ Rapport CSV généré")

def afficher_resume(resultats):
    ouverts = [r for r in resultats if "OUVERT" in r["statut"]]

    print(f"\n{'='*60}")
    print(f"📊 RÉSUMÉ : {len(ouverts)} port(s) ouvert(s)")
    print(f"{'='*60}")

    for r in ouverts:
        print(f"⚠️ Port {r['port']} ({r['service']}) — {r['risque']}")

# ─────────────────────────────────────────
# ANALYSE FICHIERS
# ─────────────────────────────────────────

def verifier_fichiers():
    print("\n🔎 Analyse des fichiers suspects")

    for fichier in FICHIERS_SUSPECTS:
        if os.path.exists(fichier):
            print(f"⚠️ Fichier suspect trouvé : {fichier}")
        else:
            print(f"✅ OK : {fichier}")

# ─────────────────────────────────────────
# ANALYSE PROCESSUS
# ─────────────────────────────────────────

def verifier_processus():
    print("\n⚙️ Analyse des processus")

    systeme = platform.system()

    try:
        if systeme == "Windows":
            output = subprocess.check_output("tasklist", shell=True).decode("cp1252", errors="ignore")
        else:
            output = subprocess.check_output("ps aux", shell=True).decode()

        for proc in PROCESSUS_SUSPECTS:
            if f"{proc}.exe" in output.lower():
                print(f"⚠️ Processus suspect détecté : {proc}")
            else:
                print(f"✅ OK : {proc}")

    except Exception as e:
        print("Erreur analyse processus :", e)

# ─────────────────────────────────────────
# ANALYSE LOGS
# ─────────────────────────────────────────

def analyser_logs():
    print("\n📜 Analyse des logs SSH")

    if platform.system() == "Windows":
        print("⚠️ Analyse logs non dispo sur Windows")
        return

    try:
        with open("/var/log/auth.log", "r") as f:
            lignes = f.readlines()

        tentatives = [l for l in lignes if "Failed password" in l]
        print(f"⚠️ Tentatives échouées : {len(tentatives)}")

    except Exception as e:
        print("Erreur logs :", e)

# ─────────────────────────────────────────
# SCORE
# ─────────────────────────────────────────

def calculer_score(resultats):
    score = 10
    ouverts = [r for r in resultats if "OUVERT" in r["statut"]]

    score -= len(ouverts)
    if score < 0:
        score = 0

    print(f"\n📊 Score sécurité : {score}/10")

    if score >= 8:
        print("✅ Système sécurisé")
    elif score >= 5:
        print("⚠️ Sécurité moyenne")
    else:
        print("❌ Système vulnérable")

# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

if __name__ == "__main__":
    resultats = lancer_audit(CIBLE)
    exporter_json(resultats)
    exporter_csv(resultats)
    afficher_resume(resultats)

    verifier_fichiers()
    verifier_processus()
    analyser_logs()

    calculer_score(resultats)