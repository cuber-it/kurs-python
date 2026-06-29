# Tag 5 – __str__ & __repr__
#
# Gibt man ein Objekt direkt aus, kommt erstmal nur Kryptisches:
#   <__main__.Hund object at 0x7f3a...>
# Mit zwei "Dunder"-Methoden (double underscore) machen wir die Ausgabe lesbar.
#
#   __str__   -> für MENSCHEN: was print(obj) und str(obj) zeigen
#   __repr__  -> für ENTWICKLER: eindeutig, idealerweise wie der Code zum Erzeugen
#                (das zeigt die interaktive Shell und repr(obj))

class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

ohne = Hund("Rex", 3)
print(ohne)                        # <__main__.Hund object at 0x...>   (unschön)

# --- Mit __str__ ---
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        return f"{self.name} ({self.alter} Jahre)"

rex = Hund("Rex", 3)
print(rex)                         # Rex (3 Jahre)
print(str(rex))                    # Rex (3 Jahre)
print(f"Mein Hund: {rex}")         # Mein Hund: Rex (3 Jahre)   (f-String nutzt __str__)

# --- __repr__: eindeutig, gut zum Debuggen ---
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Faustregel: so, dass man den Ausdruck zurück-kopieren könnte
        return f"Punkt({self.x}, {self.y})"

p = Punkt(2, 5)
print(p)                           # Punkt(2, 5)   (fehlt __str__, springt print auf __repr__ ein)
print(repr(p))                     # Punkt(2, 5)
print([Punkt(0, 0), Punkt(1, 1)])  # [Punkt(0, 0), Punkt(1, 1)]   (Listen nutzen __repr__!)

# --- Beide zusammen: __str__ schön, __repr__ technisch ---
class Konto:
    def __init__(self, inhaber, stand=0.0):
        self.inhaber = inhaber
        self.stand = stand

    def __str__(self):
        return f"Konto {self.inhaber}: {self.stand:.2f} EUR"

    def __repr__(self):
        return f"Konto(inhaber={self.inhaber!r}, stand={self.stand!r})"

k = Konto("Anna", 70.0)
print(k)                           # Konto Anna: 70.00 EUR        (print -> __str__)
print(repr(k))                     # Konto(inhaber='Anna', stand=70.0)

# Praxistipp: Hat man nur Zeit/Lust für EINE Methode, nimm __repr__.
# Fehlt __str__, fällt print() automatisch auf __repr__ zurück – aber nicht umgekehrt.
