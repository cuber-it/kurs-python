# Tag 4 – Import-Varianten & __name__
#
# Vertiefung zu den Imports: woher Python Module holt, und der
# wichtige Schalter if __name__ == "__main__".

# --- Module aus der Standardbibliothek (immer dabei, kein pip nötig) ---
import math
print(math.sqrt(16))                   # 4.0
print(math.pi)                         # 3.141592653589793

# --- from ... import: einzelne Namen direkt holen ---
from math import sqrt, pi
print(sqrt(25))                        # 5.0
print(pi)                              # 3.141592653589793

# --- as: umbenennen (bei langen Namen / Konventionen) ---
import datetime as dt
print(dt.date.today())                 # z.B. 2026-06-02

# --- from ... import * : ALLES holen -> bitte VERMEIDEN ---
# from math import *
# Problem: man sieht nicht mehr, woher ein Name kommt, und Namen
# können sich gegenseitig überschreiben. Explizit ist besser.

# --- Wo sucht Python die Module? (der Suchpfad) ---
import sys
# sys.path ist eine Liste von Ordnern, die durchsucht werden:
print(sys.path[0])                     # üblicherweise der Ordner des Skripts
# Deshalb findet "import geometrie" die Datei im selben Ordner.

# --- if __name__ == "__main__": ---
# Jede Datei hat eine eingebaute Variable __name__.
#   - Wird die Datei DIREKT gestartet:   __name__ == "__main__"
#   - Wird sie IMPORTIERT:               __name__ == "<modulname>"
print("Dieses Skript heißt:", __name__)   # "__main__" beim Direktstart

# Praktischer Nutzen: Testcode/Beispiele, die nur beim Direktstart laufen,
# aber NICHT beim Import stören (siehe geometrie.py aus 05).
def haupt():
    print("Programmstart!")

if __name__ == "__main__":
    haupt()
