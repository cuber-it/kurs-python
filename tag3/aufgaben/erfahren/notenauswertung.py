# Aufgabe (erfahren): Notenauswertung
#
# Gegeben ist eine Liste von Schüler-Datensätzen (je ein dict).
# Werte die Daten aus:
#
#   1. Durchschnittsnote aller Schüler (auf 2 Stellen).
#   2. Bester Schüler (kleinste Note = beste Note).
#   3. Gruppiere die Namen nach "bestanden" (Note <= 4) und "durchgefallen".
#
# Techniken: List Comprehension, sum/len, min(... key=...), defaultdict.
# In Deutschland: 1 = sehr gut ... 6 = ungenügend, ab 5 durchgefallen.

from collections import defaultdict

# E (Eingabe / gegeben)
schueler = [
    {"name": "Anna", "note": 2},
    {"name": "Ben",  "note": 5},
    {"name": "Cem",  "note": 1},
    {"name": "Dora", "note": 4},
    {"name": "Emil", "note": 5},
]

# V (Verarbeitung)
# 1) noten = [s["note"] for s in schueler]   -> Durchschnitt = sum/len
# 2) bester = min(schueler, key=lambda s: s["note"])
# 3) gruppen = defaultdict(list)
#    for s in schueler: Schlüssel "bestanden"/"durchgefallen" je nach Note
# ...

# A (Ausgabe)
# - "Durchschnitt: X.XX"
# - "Bester: NAME (Note N)"
# - "Bestanden: [...]"  /  "Durchgefallen: [...]"
# ...
