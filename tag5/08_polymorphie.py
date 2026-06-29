# Tag 5 – Polymorphie
#
# Polymorphie ("Vielgestaltigkeit"): Verschiedene Objekte reagieren auf
# DENSELBEN Methodenaufruf jeweils auf IHRE Art. Der aufrufende Code muss
# nicht wissen, welche Klasse genau dahintersteckt – er ruft nur die Methode.

class Hund:
    def laut_geben(self):
        return "Wuff!"

class Katze:
    def laut_geben(self):
        return "Miau!"

class Ente:
    def laut_geben(self):
        return "Quak!"

# Ein und dieselbe Schleife arbeitet mit allen drei Klassen:
tiere = [Hund(), Katze(), Ente()]
for tier in tiere:
    print(tier.laut_geben())       # Wuff! / Miau! / Quak!

# --- Duck Typing: "Wenn es quakt wie eine Ente..." ---
# Python fragt nicht nach dem Typ, sondern probiert die Methode einfach.
# Es zählt, was ein Objekt KANN, nicht von welcher Klasse es ist.
# Diese drei sind NICHT verwandt (keine gemeinsame Basisklasse) – egal,
# Hauptsache sie haben alle laut_geben().

def chor(tiere):
    """Funktioniert mit allem, das laut_geben() versteht."""
    return " ".join(t.laut_geben() for t in tiere)

print(chor(tiere))                 # Wuff! Miau! Quak!

class Roboter:
    def laut_geben(self):
        return "Beep!"

print(chor([Hund(), Roboter()]))   # Wuff! Beep!   (Roboter passt einfach dazu)

# --- Eingebaute Polymorphie: len() und + arbeiten längst so ---
print(len("hallo"))                # 5    str
print(len([1, 2, 3]))              # 3    list
print(len({"a": 1}))               # 1    dict
# len() ruft intern die __len__-Methode des jeweiligen Objekts auf.

# --- Eigene Klasse "polymorph" machen: Dunder-Methoden ---
# Indem wir die passenden __…__-Methoden definieren, fügt sich unser Objekt
# in Pythons Standardverhalten ein (len(), +, ==, < ...).
class Strecke:
    def __init__(self, *punkte):
        self.punkte = list(punkte)

    def __len__(self):             # len(obj) ruft das hier
        return len(self.punkte)

    def __add__(self, andere):     # obj1 + obj2 ruft das hier
        return Strecke(*self.punkte, *andere.punkte)

    def __repr__(self):
        return f"Strecke{tuple(self.punkte)}"

s1 = Strecke("A", "B")
s2 = Strecke("C", "D", "E")
print(len(s1))                     # 2
print(s1 + s2)                     # Strecke('A', 'B', 'C', 'D', 'E')

# Kernidee: Nicht über den Typ verzweigen (if isinstance(...)), sondern
# Objekte dieselbe Methode/Schnittstelle anbieten lassen. Das hält Code offen
# für neue Klassen, ohne ihn anzufassen.
