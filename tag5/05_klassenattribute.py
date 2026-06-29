# Tag 5 – Klassen- vs. Instanzattribute
#
# Instanzattribut: gehört zu EINEM Objekt (in __init__ per self gesetzt).
# Klassenattribut:  gehört zur KLASSE und ist für ALLE Objekte gleich/geteilt.
#                   Es steht direkt im Klassenkörper, nicht in __init__.

class Hund:
    art = "Canis lupus familiaris"     # Klassenattribut: bei allen gleich

    def __init__(self, name):
        self.name = name               # Instanzattribut: pro Objekt eigen

rex = Hund("Rex")
bella = Hund("Bella")

print(rex.name, bella.name)        # Rex Bella           (verschieden)
print(rex.art, bella.art)          # ...familiaris ...familiaris   (gleich)
print(Hund.art)                    # auch über die Klasse erreichbar

# --- Typischer Einsatz: ein gemeinsamer Zähler ---
class Konto:
    anzahl = 0                     # zählt ALLE jemals erzeugten Konten

    def __init__(self, inhaber):
        self.inhaber = inhaber
        Konto.anzahl += 1          # bewusst über die KLASSE hochzählen

a = Konto("Anna")
b = Konto("Ben")
c = Konto("Cara")
print(Konto.anzahl)                # 3

# --- Die Falle: Zuweisung über das Objekt legt ein INSTANZattribut an ---
# rex.art = "..." ändert NICHT das Klassenattribut, sondern überdeckt es nur
# für rex. bella sieht weiterhin das Original.
rex.art = "Sonderfall"
print(rex.art)                     # Sonderfall          (eigenes Instanzattribut)
print(bella.art)                   # ...familiaris       (Klassenattribut, unberührt)
print(Hund.art)                    # ...familiaris       (Klasse selbst unberührt)

# Deshalb beim Zähler oben bewusst "Konto.anzahl += 1" und NICHT "self.anzahl += 1":
# self.anzahl += 1 würde beim ersten Mal ein Instanzattribut anlegen und der
# gemeinsame Zähler bliebe stehen.

# --- Zweite Falle: VERÄNDERLICHE Klassenattribute werden GETEILT ---
# Eine Liste als Klassenattribut ist EIN Objekt für alle – gefährlich:
class FalscheGruppe:
    mitglieder = []                # geteilt von allen Instanzen!

    def __init__(self, name):
        self.mitglieder.append(name)   # hängt in die EINE gemeinsame Liste

g1 = FalscheGruppe("Anna")
g2 = FalscheGruppe("Ben")
print(g1.mitglieder)               # ['Anna', 'Ben']   <- g2 hat g1 "verschmutzt"!

# Richtig: veränderliche Daten pro Objekt in __init__ anlegen:
class RichtigeGruppe:
    def __init__(self, name):
        self.mitglieder = [name]   # jede Instanz bekommt ihre eigene Liste

r1 = RichtigeGruppe("Anna")
r2 = RichtigeGruppe("Ben")
print(r1.mitglieder, r2.mitglieder)    # ['Anna'] ['Ben']   (getrennt)
