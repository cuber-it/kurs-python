# Tag 5 – @dataclass (moderne Abkürzung)
#
# Bei reinen "Daten-Klassen" wiederholt sich viel Tipparbeit: __init__, das
# Zuweisen aller Attribute, __repr__, __eq__. @dataclass erzeugt das alles
# automatisch aus den Feldangaben. Seit Python 3.7 in der Standardbibliothek.

from dataclasses import dataclass, field

# --- Vorher: alles von Hand ---
class PunktAlt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PunktAlt(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# --- Nachher: dasselbe als Dataclass ---
@dataclass
class Punkt:
    x: int                         # Typ-Angabe ist hier Pflicht
    y: int

p1 = Punkt(2, 5)
p2 = Punkt(2, 5)
print(p1)                          # Punkt(x=2, y=5)   (__repr__ geschenkt)
print(p1 == p2)                    # True              (__eq__ geschenkt: Wertevergleich!)
# Zur Erinnerung: normale Objekte wären nur gleich, wenn es DASSELBE Objekt ist.

# --- Default-Werte ---
@dataclass
class Konto:
    inhaber: str
    stand: float = 0.0             # Default wie bei Funktionen

k = Konto("Anna")
print(k)                           # Konto(inhaber='Anna', stand=0.0)

# --- Veränderliche Defaults: NICHT [] direkt, sondern field(default_factory=...) ---
# (Dieselbe Falle wie bei Funktionen mit liste=[] – Dataclass verbietet sie sogar.)
@dataclass
class Gruppe:
    name: str
    mitglieder: list = field(default_factory=list)   # jede Instanz: eigene Liste

g1 = Gruppe("A")
g2 = Gruppe("B")
g1.mitglieder.append("Anna")
print(g1.mitglieder, g2.mitglieder)    # ['Anna'] []   (getrennt – richtig)

# --- Methoden gehen weiterhin ganz normal ---
@dataclass
class Rechteck:
    breite: float
    hoehe: float

    def flaeche(self):
        return self.breite * self.hoehe

print(Rechteck(4, 3).flaeche())    # 12

# --- frozen=True: unveränderliches Objekt (wie ein Tupel) ---
@dataclass(frozen=True)
class Farbe:
    r: int
    g: int
    b: int

c = Farbe(255, 0, 0)
print(c)                           # Farbe(r=255, g=0, b=0)
# c.r = 0                          # -> FrozenInstanceError (schützt vor Änderung)

# --- Wann was? ---
# @dataclass: wenn das Objekt vor allem DATEN bündelt (Konfig, Messpunkt, Record).
# Normale Klasse: wenn viel Verhalten/Logik im Vordergrund steht oder das
#                 Erzeugen komplexer ist als "Felder zuweisen".
# Beides ist OOP – dataclass spart nur den Boilerplate-Teil.
