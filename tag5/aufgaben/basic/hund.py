# Aufgabe (basic): Eine Klasse Hund
#
# Ziel: Übe Attribute, Methoden und eine Methode, die den Zustand ändert.
#
# Anforderungen:
#   - __init__(self, name, alter): speichert name und alter
#   - bellen(self): gibt z. B. "Rex: Wuff!" aus
#   - geburtstag(self): erhöht das Alter um 1
#   - __str__(self): liefert z. B. "Rex (3 Jahre)"
#
# Schritt 1: class Hund: und __init__ mit name und alter.
# Schritt 2: bellen – nutzt self.name im f-String.
# Schritt 3: geburtstag – self.alter += 1.
# Schritt 4: __str__ – "name (alter Jahre)".
#
# Bonus 1: Attribut self.tricks = [] in __init__ (eigene Liste pro Hund!) und
#          eine Methode trick_lernen(self, trick), die an die Liste anhängt.
# Bonus 2: Klassenattribut beine = 4, das alle Hunde teilen.

# class Hund:
#     def __init__(self, name, alter):
#         ...
#
#     def bellen(self):
#         ...
#
#     def geburtstag(self):
#         ...
#
#     def __str__(self):
#         return ...

# --- Test (einkommentieren, wenn die Klasse steht) ---
# rex = Hund("Rex", 3)
# bella = Hund("Bella", 5)
# rex.bellen()             # Rex: Wuff!
# rex.geburtstag()
# print(rex)               # Rex (4 Jahre)
# print(bella)             # Bella (5 Jahre)   <- unabhängig von rex
