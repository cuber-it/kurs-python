# Tag 4 – Tour durch die Standardbibliothek
#
# "Batteries included": Python bringt viele nützliche Module von Haus aus mit.
# Eine kleine Auswahl der häufigsten – ohne pip, einfach importieren.

# --- math: Mathematik ---
import math
print(math.sqrt(2))                    # 1.4142135623730951
print(math.floor(3.7), math.ceil(3.2)) # 3 4
print(math.factorial(5))               # 120

# --- random: Zufall (vgl. Lotto aus Tag 3) ---
import random
print(random.randint(1, 6))            # Würfel: 1..6
print(random.choice(["Kopf", "Zahl"])) # zufällige Auswahl
mische = [1, 2, 3, 4, 5]
random.shuffle(mische)                 # mischt in place
print(mische)

# --- datetime: Datum & Zeit ---
from datetime import date, datetime, timedelta
heute = date.today()
print(heute)                           # z.B. 2026-06-02
print(heute + timedelta(days=7))       # eine Woche später
jetzt = datetime.now()
print(jetzt.strftime("%d.%m.%Y %H:%M")) # formatiert: 02.06.2026 14:30

# --- collections: Counter & defaultdict (kennen wir aus Tag 3) ---
from collections import Counter
print(Counter("mississippi"))          # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# --- os & pathlib: Dateien & Pfade ---
import os
print(os.getcwd())                     # aktuelles Arbeitsverzeichnis

from pathlib import Path
p = Path(".")                          # moderner, objektorientierter Weg
print([f.name for f in p.glob("*.py")][:3])  # erste 3 .py-Dateien hier

# --- json: Daten lesen/schreiben (vgl. Tag 2) ---
import json
daten = {"name": "Anna", "alter": 30}
text = json.dumps(daten)               # dict -> JSON-String
print(text)                            # {"name": "Anna", "alter": 30}
print(json.loads(text))                # JSON-String -> dict zurück

# Tipp: Die volle Liste steht in der Doku unter
# https://docs.python.org/3/library/  – reinschauen lohnt sich!
