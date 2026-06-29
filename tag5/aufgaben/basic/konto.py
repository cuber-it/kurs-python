# Aufgabe (basic): Eine Klasse Konto
#
# Ziel: Baue eine Klasse Konto mit Attributen und Methoden – der Klassiker
# zum Üben von __init__, self und zustandsändernden Methoden.
#
# Anforderungen:
#   - __init__(self, inhaber, stand=0.0): speichert inhaber und stand
#   - einzahlen(self, betrag): erhöht den Stand (nur positive Beträge!)
#   - abheben(self, betrag): verringert den Stand, aber NICHT ins Minus
#                            (bei zu wenig Guthaben: Meldung + nichts abheben)
#   - __str__(self): liefert z. B. "Konto Anna: 70.00 EUR"
#
# Schritt 1: class Konto: und __init__ mit inhaber und stand (Default 0.0).
# Schritt 2: einzahlen – self.stand erhöhen, negative Beträge abweisen.
# Schritt 3: abheben – vorher prüfen, ob genug Guthaben da ist.
# Schritt 4: __str__ mit f-String und 2 Nachkommastellen ({self.stand:.2f}).
#
# Bonus: Methode ueberweisen(self, ziel, betrag), die von diesem Konto abhebt
#        und auf ein anderes Konto-Objekt einzahlt (Tipp: ziel.einzahlen(...)).

# class Konto:
#     def __init__(self, inhaber, stand=0.0):
#         ...
#
#     def einzahlen(self, betrag):
#         ...
#
#     def abheben(self, betrag):
#         ...
#
#     def __str__(self):
#         return ...

# --- Test (einkommentieren, wenn die Klasse steht) ---
# k = Konto("Anna", 50.0)
# k.einzahlen(20.0)
# print(k)                 # Konto Anna: 70.00 EUR
# k.abheben(100.0)         # Meldung: nicht genug Guthaben
# k.abheben(30.0)
# print(k)                 # Konto Anna: 40.00 EUR
