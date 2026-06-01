# Aufgabe (erfahren): Lottobude NG – Tipp gegen Ziehung prüfen
#
# Baut auf lottobude.py auf. Jetzt vergleichen wir einen Tipp mit der Ziehung.
#
#   1. Lass den Spieler 6 Zahlen eingeben (oder nimm einen festen Tipp).
#   2. Ziehe 6 verschiedene Gewinnzahlen (1..49).
#   3. Wie viele RICHTIGE hat der Spieler? -> Schnittmenge der beiden Sets!
#   4. Gib die richtigen Zahlen sortiert aus und die Anzahl der Treffer.
#
# Königsdisziplin (optional):
#   5. Simuliere 1.000.000 Ziehungen gegen EINEN festen Tipp und zähle,
#      wie oft 0,1,2,3,4,5,6 Richtige vorkamen (dict oder Counter).
#      -> zeigt eindrucksvoll, wie unwahrscheinlich 6 Richtige sind.
#
# Kernidee: treffer = set(tipp) & set(ziehung)  -> len(treffer) = Anzahl richtig.

import random
from collections import Counter

# E (Eingabe / gegeben)
tipp = {7, 13, 19, 23, 31, 42}          # fester Beispieltipp (Set!)

# V (Verarbeitung)
# - ziehung = set(random.sample(range(1, 50), 6))
# - treffer = tipp & ziehung
# - anzahl  = len(treffer)
#
# Für die Simulation (Punkt 5):
#   statistik = Counter()
#   for _ in range(1_000_000):
#       z = set(random.sample(range(1, 50), 6))
#       statistik[len(tipp & z)] += 1
# ...

# A (Ausgabe)
# - "Ziehung:", sorted(ziehung)
# - "Richtige:", sorted(treffer), f"({anzahl} Treffer)"
# - bei Simulation: für 0..6 die Häufigkeit ausgeben
# ...
