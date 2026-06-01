# Tag 3 – Arbeitstechniken mit Dict
#
# Die Techniken, die im Alltag am häufigsten gebraucht werden:
# zählen, gruppieren, umformen, nach Wert sortieren.

# --- Dict Comprehension ---
# analog zur List Comprehension, nur mit  schluessel: wert
zahlen = [1, 2, 3, 4]
quadrate = {n: n ** 2 for n in zahlen}
print(quadrate)                # {1: 1, 2: 4, 3: 9, 4: 16}

# zwei Listen zu einem dict verbinden (mit zip):
namen = ["Anna", "Ben", "Cem"]
alter = [30, 25, 41]
leute = {name: a for name, a in zip(namen, alter)}
print(leute)                   # {'Anna': 30, 'Ben': 25, 'Cem': 41}
# (Kurzform: dict(zip(namen, alter)) tut dasselbe)

# --- Häufigkeiten zählen (von Hand) ---
text = "banane"
zaehler = {}
for zeichen in text:
    zaehler[zeichen] = zaehler.get(zeichen, 0) + 1
print(zaehler)                 # {'b': 1, 'a': 2, 'n': 2, 'e': 1}

# --- ... das Gleiche elegant mit collections.Counter ---
from collections import Counter
print(Counter("banane"))               # Counter({'a': 2, 'n': 2, 'b': 1, 'e': 1})
print(Counter("banane").most_common(2))# [('a', 2), ('n', 2)]   (Top 2)

# --- Gruppieren mit defaultdict ---
# defaultdict legt fehlende Schlüssel automatisch mit Standardwert an.
from collections import defaultdict
woerter = ["Apfel", "Birne", "Ananas", "Banane", "Clementine"]
nach_anfang = defaultdict(list)        # fehlender Schlüssel -> leere Liste
for wort in woerter:
    nach_anfang[wort[0]].append(wort)  # kein KeyError mehr nötig
print(dict(nach_anfang))               # {'A': ['Apfel', 'Ananas'], 'B': [...], ...}

# --- Nach Wert sortieren ---
lager = {"apfel": 50, "birne": 20, "kirsche": 120}

# items() nach dem Wert (Element [1] des Paares) sortieren:
sortiert = sorted(lager.items(), key=lambda paar: paar[1], reverse=True)
print(sortiert)                # [('kirsche', 120), ('apfel', 50), ('birne', 20)]

# als dict zurück (dicts behalten seit Python 3.7 die Einfügereihenfolge):
print(dict(sortiert))          # {'kirsche': 120, 'apfel': 50, 'birne': 20}
