# Tag 4 – Funktionen (Grundlagen)
#
# Eine Funktion bündelt Code unter einem Namen. Man schreibt sie EINMAL
# und ruft sie BELIEBIG OFT auf. Das spart Wiederholung und macht Code lesbar.

# --- Definition mit def ---
def begruessung():
    print("Hallo zusammen!")

# Definieren allein tut noch nichts – erst der AUFRUF führt sie aus:
begruessung()                  # Hallo zusammen!
begruessung()                  # Hallo zusammen!   (beliebig oft)

# --- Mit Parameter (Eingabe in die Funktion) ---
def begruesse(name):
    print(f"Hallo {name}!")

begruesse("Anna")              # Hallo Anna!
begruesse("Ben")               # Hallo Ben!

# --- return: ein Ergebnis ZURÜCKGEBEN (statt nur ausgeben) ---
def quadrat(zahl):
    return zahl * zahl

ergebnis = quadrat(5)          # Rückgabe landet in der Variable
print(ergebnis)                # 25
print(quadrat(3) + quadrat(4)) # 9 + 16 = 25   (weiterrechnen möglich)

# --- WICHTIG: return ist NICHT print ---
# print zeigt nur etwas an. return liefert einen Wert zum Weiterverwenden.
def mit_print(x):
    print(x * 2)               # zeigt an, gibt aber None zurück

def mit_return(x):
    return x * 2               # liefert den Wert

a = mit_print(10)              # zeigt 20 an
print(a)                       # None   <- es kam nichts zurück!
b = mit_return(10)             # zeigt nichts an
print(b)                       # 20     <- der Wert ist nutzbar

# --- Funktion ohne return liefert None ---
def nichts():
    pass                       # macht bewusst nichts
print(nichts())                # None

# --- Docstring: Kurzbeschreibung direkt unter def (gute Gewohnheit!) ---
def addiere(a, b):
    """Gibt die Summe von a und b zurück."""
    return a + b

print(addiere(2, 3))           # 5
print(addiere.__doc__)         # Gibt die Summe von a und b zurück.
