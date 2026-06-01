# Tag 3 – Tupel
#
# Ein Tupel ist wie eine Liste – aber UNVERÄNDERLICH (immutable).
# Gut für feste Zusammengehörigkeiten: Koordinaten, RGB-Werte,
# Rückgaben mehrerer Werte aus einer Funktion.

# --- Erstellen ---
punkt = (3, 4)
farbe = (255, 128, 0)
einzeln = (42,)                # ACHTUNG: das Komma macht das Tupel!
keintupel = (42)               # das ist nur die Zahl 42 in Klammern
print(type(einzeln))           # <class 'tuple'>
print(type(keintupel))         # <class 'int'>

# Klammern sind oft optional:
auch_ein_tupel = 1, 2, 3
print(auch_ein_tupel)          # (1, 2, 3)

# --- Zugriff wie bei Listen ---
print(punkt[0])                # 3
print(farbe[-1])               # 0

# --- aber: kein Ändern! ---
# punkt[0] = 9   -> TypeError: 'tuple' object does not support item assignment

# --- Packing & Unpacking (sehr praktisch!) ---
x, y = punkt                   # entpacken in zwei Variablen
print(x, y)                    # 3 4

# Klassiker: Werte tauschen ganz ohne Hilfsvariable
a, b = 1, 2
a, b = b, a
print(a, b)                    # 2 1

# Funktionen können "mehrere Werte" zurückgeben (= ein Tupel)
def min_max(werte):
    return min(werte), max(werte)

kleinste, groesste = min_max([7, 2, 9, 4])
print(kleinste, groesste)      # 2 9

# --- Faustregel ---
# Liste  -> Inhalt ändert sich (Sammlung gleichartiger Dinge)
# Tupel  -> feste, zusammengehörige Werte, die so bleiben sollen
