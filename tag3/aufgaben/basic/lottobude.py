# Aufgabe (basic): Lottobude – 6 aus 49 ziehen
#
# Ziehe einen zufälligen Lottotipp: 6 verschiedene Zahlen aus 1 bis 49.
#
# Worauf es ankommt:
#   - Die 6 Zahlen müssen VERSCHIEDEN sein (keine Dublette!).
#   - Am Ende sortiert ausgeben.
#
# Zwei Wege – probiere beide:
#   A) mit einem Set: in einer Schleife zufällige Zahlen ziehen und ins Set
#      legen, bis len(set) == 6 ist (Duplikate fallen automatisch weg).
#   B) eleganter mit random.sample(bereich, 6) – zieht direkt 6 verschiedene.
#
# Tipp: range(1, 50) liefert die Zahlen 1..49 (50 ist exklusiv!).

import random

# E (Eingabe / gegeben)
# - Eine Benutzereingabe, die validiert werden muss:
#    - 6 Elemente
#    - alles integer bzw zu int wandelbar
#    - keine Doubletten
#    - alle zwischen 1 und 49
# Wenn das zutrifft gehts weiter. Sonst Fehlermeldung was ist und Abbruch
eingabe = input("Ihr Tipp: ").split(" ")

if len(eingabe) != 6:
    print("Ungültige Anzahl")
    exit(1)

tipp = []
for zahl in eingabe:
    try:
        zahl = int(zahl)
        if zahl < 1 or zahl > 49:
            print("Ungültiger Wertebereich")
            exit(3)
        if zahl in tipp:
            print("Doppelter Wert")
            exit(4)
        tipp.append(zahl)
    except ValueError:
        print("Kein Zahelnwert")
        exit(2)

print("Tipp:",tipp)

# V (Verarbeitung)
# Weg A:
#   tipp = set()
#   while len(tipp) < 6:
#       tipp.add(random.randint(1, 49))
# Weg B:
#   tipp = random.sample(range(1, 50), 6)
# ...

# A (Ausgabe)
# - sortiert ausgeben: print("Dein Tipp:", sorted(tipp))
# ...
