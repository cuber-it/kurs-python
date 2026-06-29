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

DATEI = r"/home/ucuber/Workspace/kurse/kurs-python/tag5/aufgaben/gegenparteien.txt"
LIMIT = Decimal("5000000")


class Gegenpartei:
    GEWICHT = {
        "AAA": Decimal("0.2"), "AA": Decimal("0.4"), "A": Decimal("0.6"),
        "BBB": Decimal("0.8"), "BB": Decimal("1.0"), "B": Decimal("1.5"),
        "CCC": Decimal("2.0"),
    }

    def __init__(self, name, rating, exposure):
        self.name = name
        self.rating = rating
        self.exposure = Decimal(exposure)

    def gewichtet(self):
        return self.exposure * self.GEWICHT.get(self.rating, Decimal(1))

    def ueber(self, limit):
        return self.exposure > limit

    def __str__(self):
        return f"{self.name:<18} {self.rating:<4} {self.exposure:>14,.0f}"


class Portfolio:
    def __init__(self, parteien):
        self.parteien = parteien

    def gesamt(self):
        return sum((p.exposure for p in self.parteien), Decimal(0))

    def risikogewichtet(self):
        return sum((p.gewichtet() for p in self.parteien), Decimal(0))

    def ueber_limit(self, limit):
        return [p for p in self.parteien if p.ueber(limit)]

    def report(self, limit):
        print(f"{len(self.parteien)} Gegenparteien")
        print(f"Exposure gesamt:    {self.gesamt():,.0f} EUR")
        print(f"Risikogewichtet:    {self.risikogewichtet():,.0f} EUR")
        print(f"\nUeber Limit ({limit:,.0f} EUR):")
        for p in self.ueber_limit(limit):
            print(f"  {p}")

class App:
    def run(self, datei):
        with open(datei, encoding="utf-8") as f:
            return Portfolio([Gegenpartei(*z.split("\t")) for z in f])


if __name__ == "__main__":
    App().run(DATEI).report(LIMIT)

# Erläuterungen
# gewichtet() und ueber() gehören fachlich zur einzelnen Gegenpartei — in der prozeduralen Version
# mussten alle Funktionen das GEWICHT-dict kennen und mit rating jonglieren. Jetzt fragt das Portfolio
# einfach p.gewichtet() und muss von Ratings gar nichts wissen.
#
# GEWICHT ist Klassenattribut der Gegenpartei — es gehört dorthin, wo es gebraucht wird, nicht ins
# Modul-Global. Der eigentliche Test ist Erweiterbarkeit: Kommt morgen ein Laufzeitfaktor dazu, änderst
# du nur Gegenpartei.gewichtet() — eine Stelle, das Portfolio bleibt unberührt.
# Oder du brauchst besicherte Gegenparteien mit anderer Gewichtung: eine Unterklasse
# BesicherteGegenpartei(Gegenpartei), die gewichtet() überschreibt, und das Portfolio
# rechnet automatisch richtig (Polymorphie).
