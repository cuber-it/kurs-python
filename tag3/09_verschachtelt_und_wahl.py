# Tag 3 – Sonderkapitel: Verschachtelte Strukturen & "welche Struktur wann?"
#
# In der Praxis kombiniert man Listen, Dicts, Tupel und Sets.
# So sehen reale Daten aus (genau wie JSON aus Tag 2).

# --- Eine Liste von Dicts: der Klassiker für "Datensätze" ---
mitarbeiter = [
    {"name": "Anna", "abteilung": "IT",      "gehalt": 5000},
    {"name": "Ben",  "abteilung": "Vertrieb", "gehalt": 4200},
    {"name": "Cem",  "abteilung": "IT",      "gehalt": 4800},
]

# Zugriff: erst Index (welcher Datensatz), dann Schlüssel (welches Feld)
print(mitarbeiter[0]["name"])          # 'Anna'

# Durchlaufen:
for person in mitarbeiter:
    print(f"{person['name']}: {person['gehalt']} €")

# --- Auswerten mit den Techniken von vorhin ---
# Alle Namen (List Comprehension):
namen = [p["name"] for p in mitarbeiter]
print(namen)                           # ['Anna', 'Ben', 'Cem']

# Nach Abteilung gruppieren (defaultdict):
from collections import defaultdict
nach_abt = defaultdict(list)
for p in mitarbeiter:
    nach_abt[p["abteilung"]].append(p["name"])
print(dict(nach_abt))                  # {'IT': ['Anna', 'Cem'], 'Vertrieb': ['Ben']}

# Höchstes Gehalt finden:
top = max(mitarbeiter, key=lambda p: p["gehalt"])
print(f"Top-Gehalt: {top['name']}")    # Anna

# Durchschnittsgehalt:
gehaelter = [p["gehalt"] for p in mitarbeiter]
print(sum(gehaelter) / len(gehaelter)) # 4666.66...


# --- WELCHE STRUKTUR WANN? (Spickzettel) ---
#
#   list   []   geordnet, veränderbar, Duplikate erlaubt
#               -> Reihenfolge zählt, Sammlung gleichartiger Dinge
#
#   tuple  ()   geordnet, UNveränderlich
#               -> feste zusammengehörige Werte (Koordinate, Rückgabe)
#
#   set    {}   ungeordnet, KEINE Duplikate, sehr schnelles "in"
#               -> Eindeutigkeit, Mengenlogik (Schnitt/Vereinigung)
#
#   dict   {k:v} Schlüssel -> Wert, schneller Zugriff über Schlüssel
#               -> benannte Felder, Nachschlagen, Zuordnungen
#
# Faustregel:
#   "Etwas anhand eines Namens nachschlagen?"        -> dict
#   "Nur wissen, ob/welche Dinge vorkommen?"         -> set
#   "Reihenfolge wichtig, Inhalt ändert sich?"       -> list
#   "Fester Verbund, der so bleibt?"                 -> tuple
