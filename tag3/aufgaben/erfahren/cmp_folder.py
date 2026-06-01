# Der Inhalt zweier Ordner soll verglichen werden:
#
# - Nur Dateien
# - Alle Dateien
# - Kriterium A: der Name - Gleiche Namen -> Melden
# - Kriterium B: der Inhalt - Gleicher Inhalt -> Melden
#
# Inhalt-Test mit Hilfe des md5 Hash:
# - Bib vorhanden
# - Beispiele vorhanden
# - Vorgehen Datei öffnen, md5 berechnen - > im dict nachschauen ob es das md5 schon gibt.
# -- wenn ja, namen in einer Lsite zu dem md5 anhängen
# -- wenn nein, md5 neu eintragen als key und, akt. Dateiname dann als erster Eintrag in der Liste
import os
import hashlib

same_name = {}
same_md5 = {}

folder_a = input("Ordner A: ")
folder_b = input("Ordner B: ")

for ordner in (folder_a, folder_b):
    if not os.path.isdir(ordner):
        print(f"Fehler: '{ordner}' ist kein gültiger Ordner.")
        exit(1)

if folder_a == folder_b:
    print("Vergleich des Ordners mit sich selbst nicht erlaubt")
    exit(2)


# Funktionen um alle Namen zu bekommen von Datein die in einem Folder sind
alle_pfade = []
for ordner in (folder_a, folder_b):
    for eintrag in os.listdir(ordner):
        pfad = os.path.join(ordner, eintrag)
        if os.path.isfile(pfad):             # Unterordner aussortieren
            alle_pfade.append(pfad)

# Auswertung auf doppelte
for pfad in alle_pfade:
    name = os.path.basename(pfad)            # reiner Dateiname für Kriterium A

    # --- Kriterium A: gleicher Name ---
    if name in same_name:
        same_name[name].append(pfad)
    else:
        same_name[name] = [pfad]

    # --- Kriterium B: gleicher Inhalt (MD5) ---
    with open(pfad, "rb") as f:              # "rb" = binär lesen!
        daten = f.read()
    h = hashlib.md5(daten).hexdigest()

    same_md5[h] = same_md5.get(h, []) + [pfad] # Effekt gleich wie bei Kriterium A, nur kürzer geschrieben
    # same_md5.setdefault(h, []).append(pfad) - geht auch, etwas schneller als das Bsp oberhalb

    # --- Auswertung: nur melden, wo die Liste länger als 1 ist ---
    print("=== Gleiche Namen ===")
    for name, pfade in same_name.items():
        if len(pfade) > 1:
            print(f"{name}: {pfade}")

    print("=== Gleicher Inhalt ===")
    for h, pfade in same_md5.items():
        if len(pfade) > 1:
            print(f"{h[:8]}…: {pfade}")
