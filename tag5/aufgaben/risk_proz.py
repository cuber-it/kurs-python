# Aufgabe: Counterparty-Exposure-Report
#
# Datei gegenparteien.txt einlesen (eine pro Zeile, Tab-getrennt):
#   name <TAB> rating <TAB> exposure
# Beispielzeile:  Acme Corp	CCC	8000000
#
# Ausgeben:
#   1. Gesamt-Exposure (Summe aller exposure)
#   2. Risikogewichtetes Exposure: exposure * Gewicht je Rating, dann summieren
#   3. Alle Gegenparteien ueber einem Limit (z.B. 5_000_000)
#
# Rating-Gewichte (dict, unbekannt -> 1.0):
#   AAA:0.2  AA:0.4  A:0.6  BBB:0.8  BB:1.0  B:1.5  CCC:2.0
#
# Vorgaben:
#   - fehlende Datei abfangen (nicht abstuerzen)
#   - Betraege mit Tausendertrennzeichen: f"{wert:,.0f}"
#   - diese Lösung zeigt auch den Einsatz von Decimal, dabei gilt:
#
# Hinweise:
#
# Decimal(exposure) nimmt den String direkt — kein float dazwischen, sonst
# schleppst du dessen Ungenauigkeit wieder ein.
# Wichtig: bei Decimal("5000000") / Decimal("0.2") die Zahl als String übergeben,
# nicht Decimal(0.2), sonst landet der krumme Float-Wert in der Decimal.
# Beim sum der Startwert Decimal(0) — sonst beginnt sum mit dem int 0 und mischt die Typen.
# Die {:,.0f}-Formatierung funktioniert mit Decimal genauso.
#
# Loesungsweg frei: a) prozedural  oder  b) OOP (Gegenpartei + Portfolio)
# Alles in eine Datei.
from decimal import Decimal

GEWICHT = {
    "AAA": Decimal("0.2"), "AA": Decimal("0.4"), "A": Decimal("0.6"),
    "BBB": Decimal("0.8"), "BB": Decimal("1.0"), "B": Decimal("1.5"),
    "CCC": Decimal("2.0"),
}
DATEI = r"/home/ucuber/Workspace/kurse/kurs-python/tag5/aufgaben/gegenparteien.txt"
LIMIT = Decimal("5000000")


def lesen():
    with open(DATEI, encoding="utf-8") as f:
        return [(name, rating, Decimal(exposure)) for name, rating, exposure in (z.split("\t") for z in f)]


def gesamt(gp):
    return sum((exposure for name, rating, exposure in gp), Decimal(0))


def risikogewichtet(gp):
    return sum((exposure * GEWICHT.get(rating, Decimal(1)) for name, rating, exposure in gp), Decimal(0))


def ueber_limit(gp):
    return [(name, rating, exposure) for name, rating, exposure in gp if exposure > LIMIT]


def report(gp):
    print(f"{len(gp)} Gegenparteien")
    print(f"Exposure gesamt:    {gesamt(gp):,.0f} EUR")
    print(f"Risikogewichtet:    {risikogewichtet(gp):,.0f} EUR")
    print(f"\nUeber Limit ({LIMIT:,.0f} EUR):")
    for name, rating, exposure in ueber_limit(gp):
        print(f"  {name:<18} {rating:<4} {exposure:>14,.0f}")


if __name__ == "__main__":
    report(lesen())
