# Tag 5 – __init__ & Attribute
#
# In 01 haben wir Attribute von außen drangeschraubt (rex.name = "Rex").
# Das ist fehleranfällig: Vergisst man eins, ist das Objekt halb leer.
#
# Besser: Beim Erzeugen gleich alles mitgeben. Dafür gibt es __init__ –
# den KONSTRUKTOR. Er läuft automatisch, sobald ein Objekt entsteht.

# --- self: der Platzhalter für "dieses eine Objekt" ---
# Jede Methode bekommt als ERSTES Argument das Objekt selbst – per Konvention
# "self" genannt. Über self gehören Attribute zu GENAU diesem Objekt.

class Hund:
    def __init__(self, name, alter):
        # self.name ist das ATTRIBUT des Objekts,
        # name (rechts) ist der Parameter aus dem Aufruf.
        self.name = name
        self.alter = alter

# Beim Erzeugen die Werte übergeben – __init__ wird automatisch aufgerufen.
# Achtung: self NICHT selbst mitgeben, das macht Python.
rex = Hund("Rex", 3)
bella = Hund("Bella", 5)

print(rex.name, rex.alter)         # Rex 3
print(bella.name, bella.alter)     # Bella 5

# --- Jedes Objekt hat seine EIGENEN Attribute ---
rex.alter = 4                      # nur rex altert
print(rex.alter)                   # 4
print(bella.alter)                 # 5   (unverändert)

# --- Default-Werte funktionieren wie bei normalen Funktionen ---
class Konto:
    def __init__(self, inhaber, stand=0.0):
        self.inhaber = inhaber
        self.stand = stand

k1 = Konto("Anna")                 # stand nutzt den Default 0.0
k2 = Konto("Ben", 100.0)
print(k1.inhaber, k1.stand)        # Anna 0.0
print(k2.inhaber, k2.stand)        # Ben 100.0

# --- Attribute dürfen auch aus den Parametern BERECHNET werden ---
class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe
        self.flaeche = breite * hoehe   # einmal beim Erzeugen ausgerechnet

r = Rechteck(4, 3)
print(r.flaeche)                   # 12

# Stolperfalle: Vergisst man self., entsteht nur eine lokale Variable,
# die nach __init__ wieder verschwindet:
class Falsch:
    def __init__(self, x):
        wert = x                   # KEIN Attribut! nur lokal in __init__
f = Falsch(10)
# print(f.wert)                    # -> AttributeError: 'Falsch' object has no attribute 'wert'
print(hasattr(f, "wert"))          # False
