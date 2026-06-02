# Tag 4 – pip & externe Pakete (Erläuterung)
#
# Diese Datei ERKLÄRT den Umgang mit externen Paketen. Die pip-Befehle
# gehören ins Terminal (mit aktivem venv, siehe VENV.md), nicht in den Code.
# Darum stehen sie hier als Kommentar.

# --- Was ist pip? ---
# pip ist Pythons Paketmanager. Er lädt Pakete vom "Python Package Index"
# (PyPI, https://pypi.org) und installiert sie in deine Umgebung.

# --- Typische Befehle (im Terminal, venv aktiv!) ---
#   pip install requests          # ein Paket installieren
#   pip install requests==2.31.0  # eine BESTIMMTE Version
#   pip list                      # installierte Pakete anzeigen
#   pip show requests             # Details zu einem Paket
#   pip uninstall requests        # entfernen
#   pip install --upgrade requests# aktualisieren

# --- requirements.txt: Projekt-Abhängigkeiten festhalten ---
# Eine Textdatei listet, was dein Projekt braucht – eine Zeile pro Paket:
#
#   requests==2.31.0
#   rich>=13.0
#
# Damit kann jede:r die exakt gleichen Pakete nachinstallieren:
#   pip install -r requirements.txt
#
# Aktuellen Stand einfrieren:
#   pip freeze > requirements.txt

# --- Beispiel: ein externes Paket nutzen (NACH der Installation) ---
# import requests
# antwort = requests.get("https://api.github.com")
# print(antwort.status_code)        # 200
#
# Damit dieser import klappt, muss "requests" vorher per pip installiert
# sein – im AKTIVEN venv. Ohne venv landen Pakete systemweit, was schnell
# zu Versionskonflikten zwischen Projekten führt (siehe VENV.md).

# --- Warum venv + pip zusammengehören (Kurzfassung) ---
# Jedes Projekt bekommt sein eigenes venv mit genau den Paketen, die es
# braucht. Projekt A darf requests 2.31 nutzen, Projekt B requests 2.20 –
# ohne sich in die Quere zu kommen. Das ist der Standard-Workflow.

print("Diese Datei ist zum Lesen gedacht – die echten Befehle laufen im Terminal.")
print("Siehe VENV.md für den kompletten venv-Workflow.")
