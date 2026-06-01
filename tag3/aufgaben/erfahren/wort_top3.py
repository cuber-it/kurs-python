# Aufgabe (erfahren): Die häufigsten Wörter (Top 3)
#
# Ermittle aus einem Text die drei häufigsten Wörter mit ihrer Anzahl.
#
# Anforderungen:
#   - Groß-/Kleinschreibung ignorieren
#   - Satzzeichen NICHT mitzählen (., ! ? , entfernen)
#   - Ausgabe als Rangliste: "1. wort (n x)"
#
# Techniken: str-Methoden, collections.Counter, .most_common(n).
# Tipp gegen Satzzeichen: text = text.replace(".", " ").replace(",", " ") ...
#       oder eleganter mit dem Modul "re" aus Tag 2.

from collections import Counter

# E (Eingabe / gegeben)
text = """Python ist toll. Python ist einfach, und Python macht Spass!
Listen, Dicts und Sets sind toll."""

# V (Verarbeitung)
# - bereinigen (Kleinschreibung, Satzzeichen raus) und in Wörter zerlegen
# - Counter(woerter) bauen
# - top = Counter(...).most_common(3)
# ...

# A (Ausgabe)
# - for nr, (wort, anzahl) in enumerate(top, start=1):
#       print(f"{nr}. {wort} ({anzahl} x)")
# ...
