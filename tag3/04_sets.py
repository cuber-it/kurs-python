# Tag 3 – Sets (Mengen)
#
# Ein Set ist eine UNGEORDNETE Sammlung OHNE Duplikate.
# Stark für: Duplikate entfernen, Zugehörigkeit testen, Mengenlogik.

# --- Erstellen ---
zahlen = {1, 2, 3, 3, 2}
print(zahlen)                  # {1, 2, 3}   (Duplikate fallen weg)

# ACHTUNG: leeres Set geht NICHT mit {} -- das ist ein leeres dict!
leer = set()
print(type(leer))              # <class 'set'>
print(type({}))               # <class 'dict'>

# --- Klassiker: Duplikate aus einer Liste entfernen ---
mit_dubletten = [1, 2, 2, 3, 3, 3, 4]
eindeutig = list(set(mit_dubletten))
print(eindeutig)               # z.B. [1, 2, 3, 4]  (Reihenfolge NICHT garantiert!)

# --- Zugehörigkeit testen (sehr schnell, schneller als bei Listen) ---
print(3 in zahlen)             # True
print(9 in zahlen)             # False

# --- Hinzufügen / Entfernen ---
zahlen.add(4)
print(zahlen)                  # {1, 2, 3, 4}

zahlen.discard(99)             # discard: kein Fehler, wenn nicht vorhanden
zahlen.remove(4)               # remove: KeyError, wenn nicht vorhanden
print(zahlen)                  # {1, 2, 3}

# --- Mengenoperationen (das eigentliche Highlight) ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)                   # Vereinigung   {1, 2, 3, 4, 5, 6}
print(a & b)                   # Schnittmenge  {3, 4}
print(a - b)                   # Differenz     {1, 2}     (in a, nicht in b)
print(a ^ b)                   # symm. Diff.   {1, 2, 5, 6} (in genau einem)

# als Methoden lesbarer:
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# --- Teilmengen prüfen ---
print({1, 2} <= a)             # True   (Teilmenge von a?)
print(a >= {1, 2})            # True   (Obermenge?)

# --- praktisches Beispiel: gemeinsame Interessen ---
anna = {"lesen", "kochen", "wandern"}
ben  = {"kochen", "gaming", "wandern"}
print(anna & ben)              # {'kochen', 'wandern'}   (Gemeinsamkeiten)
print(anna - ben)              # {'lesen'}               (nur Anna)

# --- frozenset: ein unveränderliches Set ---
# (kann z.B. als dict-Schlüssel oder Element eines anderen Sets dienen)
fix = frozenset({1, 2, 3})
# fix.add(4)   -> AttributeError
print(fix)                     # frozenset({1, 2, 3})
