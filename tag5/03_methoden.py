# Tag 5 – Methoden
#
# Attribute sind, was ein Objekt HAT. Methoden sind, was es KANN.
# Eine Methode ist einfach eine Funktion INNERHALB der Klasse – mit self
# als erstem Parameter, damit sie an die Attribute "ihres" Objekts kommt.

class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    # Methode, die NUR liest (und etwas zurückgibt):
    def beschreibung(self):
        return f"{self.name} ist {self.alter} Jahre alt"

    # Methode, die etwas TUT (Seiteneffekt: Ausgabe):
    def bellen(self):
        print(f"{self.name}: Wuff!")

    # Methode, die den ZUSTAND ändert (ein Attribut verändern):
    def geburtstag(self):
        self.alter += 1

rex = Hund("Rex", 3)

# Aufruf mit Punkt-Syntax: objekt.methode()
# self wird automatisch eingesetzt -> rex.bellen() entspricht Hund.bellen(rex)
print(rex.beschreibung())          # Rex ist 3 Jahre alt
rex.bellen()                       # Rex: Wuff!

rex.geburtstag()                   # ändert rex.alter
print(rex.beschreibung())          # Rex ist 4 Jahre alt

# --- Methoden dürfen andere Methoden desselben Objekts aufrufen ---
class Konto:
    def __init__(self, inhaber, stand=0.0):
        self.inhaber = inhaber
        self.stand = stand

    def einzahlen(self, betrag):
        self.stand += betrag

    def abheben(self, betrag):
        if betrag > self.stand:
            print("Nicht genug Guthaben!")
            return False           # frühes return signalisiert Fehlschlag
        self.stand -= betrag
        return True

    def info(self):
        # nutzt das Attribut – immer über self:
        return f"{self.inhaber}: {self.stand:.2f} EUR"

k = Konto("Anna", 50.0)
k.einzahlen(20.0)
print(k.info())                    # Anna: 70.00 EUR
k.abheben(100.0)                   # Nicht genug Guthaben!
print(k.abheben(30.0))             # True
print(k.info())                    # Anna: 40.00 EUR

# --- return vs. Zustand ändern: zwei verschiedene Zwecke ---
# einzahlen()/abheben() ÄNDERN den Zustand (self.stand).
# info()/beschreibung() LESEN nur und geben einen Wert zurück.
# Beides ist ok – aber bewusst wählen: rechnet die Methode etwas aus,
# oder verändert sie das Objekt?
