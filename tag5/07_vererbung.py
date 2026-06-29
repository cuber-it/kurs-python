# Tag 5 – Vererbung
#
# Vererbung: Eine Klasse baut auf einer anderen auf. Die Unterklasse erbt alle
# Attribute und Methoden der Basisklasse und kann ergänzen oder ändern.
# Ziel: gemeinsamen Code EINMAL schreiben, Besonderheiten nur dort, wo nötig.
#
#   Basisklasse / Elternklasse  -> das Allgemeine
#   Unterklasse  / Kindklasse   -> das Speziellere ("ist ein")

# --- Basisklasse mit gemeinsamem Verhalten ---
class Tier:
    def __init__(self, name):
        self.name = name

    def fressen(self):
        print(f"{self.name} frisst.")

    def laut_geben(self):
        print(f"{self.name} macht ein Geräusch.")

# --- Unterklasse: erbt von Tier (in Klammern die Basisklasse) ---
class Hund(Tier):
    def laut_geben(self):              # Methode ÜBERSCHREIBEN
        print(f"{self.name}: Wuff!")

class Katze(Tier):
    def laut_geben(self):
        print(f"{self.name}: Miau!")

rex = Hund("Rex")
rex.fressen()                      # Rex frisst.        (von Tier geerbt)
rex.laut_geben()                   # Rex: Wuff!         (überschrieben)
Katze("Mimi").laut_geben()         # Mimi: Miau!

print(isinstance(rex, Hund))       # True
print(isinstance(rex, Tier))       # True   (ein Hund IST auch ein Tier)

# --- super(): die Basisklasse mitarbeiten lassen ---
# Wenn die Unterklasse ein eigenes __init__ braucht, aber das der Basisklasse
# nicht doppeln will, ruft sie es per super() auf.
class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt

    def info(self):
        return f"{self.name}, {self.gehalt} EUR"

class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, team):
        super().__init__(name, gehalt)     # Basis-Konstruktor erledigt name/gehalt
        self.team = team                   # nur das Neue selbst setzen

    def info(self):
        basis = super().info()             # auch Methoden lassen sich erweitern
        return f"{basis}, Team: {self.team}"

m = Manager("Anna", 6000, 5)
print(m.info())                    # Anna, 6000 EUR, Team: 5
print(m.name)                      # Anna   (von Mitarbeiter geerbt)

# --- "ist ein" vs. "hat ein" ---
# Vererbung passt, wenn die Unterklasse WIRKLICH eine Spezialform ist
# (Hund IST EIN Tier, Manager IST EIN Mitarbeiter).
# Wenn etwas nur Teile enthält, ist Zusammensetzen besser:
# ein Auto HAT EINEN Motor (Attribut), es IST kein Motor.
class Motor:
    def starten(self):
        print("brumm")

class Auto:
    def __init__(self):
        self.motor = Motor()       # Komposition: Auto HAT einen Motor

    def losfahren(self):
        self.motor.starten()       # nutzt das enthaltene Objekt

Auto().losfahren()                 # brumm
