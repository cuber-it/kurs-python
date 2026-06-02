# Aufgabe (basic): Würfeln als Funktion
#
# Schreibe eine Funktion wuerfeln(anzahl), die "anzahl" Würfe (1..6) macht
# und die Augensumme ZURÜCKGIBT.
#
# Schritt 1: random importieren.
# Schritt 2: Funktion mit Parameter anzahl definieren.
# Schritt 3: in einer Schleife anzahl-mal random.randint(1, 6) ziehen
#            und aufsummieren.
# Schritt 4: Summe zurückgeben.
#
# Bonus: zusätzlich die einzelnen Würfe als Liste zurückgeben
#        (Tipp: Liste füllen und zusammen mit der Summe zurückgeben -> Tupel).

import random

# V (Verarbeitung – die Funktion)
# def wuerfeln(anzahl):
#     summe = 0
#     for _ in range(anzahl):
#         ...
#     return summe

# A (Ausgabe)
# print("Augensumme bei 3 Würfen:", wuerfeln(3))
# ...
