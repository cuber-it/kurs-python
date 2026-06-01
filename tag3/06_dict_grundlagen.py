# Tag 3 – Dict (Grundlagen)
#
# Ein Dictionary speichert Paare aus SCHLÜSSEL -> WERT.
# Zugriff nicht über Position, sondern über den Schlüssel.
# Schlüssel müssen eindeutig und unveränderlich sein (str, int, tuple ...).

# --- Erstellen ---
person = {
    "name": "Anna",
    "alter": 30,
    "stadt": "Hamburg",
}
leer = {}                      # leeres dict

# --- Zugriff über den Schlüssel ---
print(person["name"])          # 'Anna'

# Fehlender Schlüssel mit [] -> KeyError:
# print(person["beruf"])       # KeyError!

# Sicherer Zugriff mit get():
print(person.get("beruf"))             # None   (kein Fehler)
print(person.get("beruf", "unbekannt"))# 'unbekannt'  (Standardwert)

# --- Hinzufügen / Ändern (gleiche Syntax) ---
person["beruf"] = "Entwicklerin"   # neuer Schlüssel
person["alter"] = 31               # vorhandenen Wert überschreiben
print(person)

# --- Existenz prüfen mit "in" (prüft die SCHLÜSSEL) ---
print("name" in person)        # True
print("Anna" in person)        # False  (Anna ist ein WERT, kein Schlüssel)

# --- Löschen ---
del person["stadt"]            # Schlüssel entfernen
beruf = person.pop("beruf")    # entfernen UND Wert zurückgeben
print(beruf)                   # 'Entwicklerin'
print(person)

# --- Anzahl der Paare ---
print(len(person))             # 2

# --- Werte dürfen alles sein, auch Listen/dicts (verschachteln) ---
kurs = {
    "titel": "Python",
    "teilnehmer": ["Anna", "Ben"],
    "tage": {"tag1": "Basics", "tag3": "Datenstrukturen"},
}
print(kurs["teilnehmer"][0])       # 'Anna'
print(kurs["tage"]["tag3"])        # 'Datenstrukturen'
