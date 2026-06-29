# Tag 5 – kursreihe.py  (Vorführmodul, fertig & lauffähig)
#
# Das OOP-Pendant zu Tag 4 `data_source.py`. GLEICHE Daten, GLEICHE Kennzahlen –
# aber als Klasse statt als Funktionssammlung.
#
# Vergleich:
#   Tag 4 (funktional):  daten = load_sql(pfad);  mittel(daten);  sma(daten, 20)
#   Tag 5 (OOP):         reihe = Kursreihe.aus_sql(pfad);  reihe.mittel();  reihe.sma(20)
#
# Der Unterschied: Die Daten und die Funktionen, die damit arbeiten, stecken
# jetzt im selben Objekt. Man reicht nicht mehr "daten" durch jede Funktion,
# sondern fragt das Objekt direkt: reihe.hoch(), reihe.mittel(), ...

import sqlite3


class Kursreihe:
    """Eine Zeitreihe von Schlusskursen (ein Handelstag = ein Eintrag)."""

    # --- Konstruktor: bekommt fertige Daten (Liste von Dicts) ---
    def __init__(self, daten, name="Kursreihe"):
        # Defensiv kopieren und sortieren, damit das Objekt seinen Zustand besitzt:
        self.daten = sorted(daten, key=lambda d: d["date"])
        self.name = name

    # --- Alternativer Konstruktor: aus einer SQLite-DB laden ---
    # @classmethod bekommt die KLASSE (cls) statt eines Objekts. Praktisch als
    # "Fabrik": Kursreihe.aus_sql(...) liefert eine fertige Instanz zurück.
    @classmethod
    def aus_sql(cls, db_pfad, name="AAPL"):
        con = sqlite3.connect(db_pfad)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT date, close, volume FROM quotes ORDER BY date ASC")
        daten = [dict(date=r["date"], close=r["close"], volume=r["volume"])
                 for r in cur.fetchall()]
        con.close()
        return cls(daten, name=name)

    # --- Dunder: das Objekt fügt sich in Pythons Standardverhalten ein ---
    def __len__(self):
        return len(self.daten)

    def __getitem__(self, i):
        # ermöglicht reihe[0] und sogar Slicing reihe[-5:]
        return self.daten[i]

    def __str__(self):
        if not self.daten:
            return f"{self.name}: leer"
        return (f"{self.name}: {len(self.daten)} Tage "
                f"({self.daten[0]['date']} bis {self.daten[-1]['date']})")

    def __repr__(self):
        return f"Kursreihe(name={self.name!r}, tage={len(self.daten)})"

    # --- Auswahl: gibt eine NEUE Kursreihe zurück (Original bleibt unberührt) ---
    def zeitraum(self, von, bis):
        teil = [d for d in self.daten if von <= d["date"] <= bis]
        return Kursreihe(teil, name=f"{self.name} {von}..{bis}")

    # --- interne Hilfe (Konvention: _ = nicht Teil der öffentlichen Schnittstelle) ---
    def _closes(self):
        return [d["close"] for d in self.daten]

    # --- Kennzahlen ---
    def hoch(self):
        return max(self._closes())

    def tief(self):
        return min(self._closes())

    def mittel(self):
        werte = self._closes()
        return round(sum(werte) / len(werte), 2) if werte else 0.0

    def gesamtrendite(self):
        """Rendite vom ersten bis zum letzten Tag (in %)."""
        if len(self.daten) < 2:
            return 0.0
        alt, neu = self.daten[0]["close"], self.daten[-1]["close"]
        return round((neu - alt) / alt * 100, 2)

    # --- abgeleitete Eigenschaft per @property (Zugriff ohne Klammern) ---
    @property
    def spanne(self):
        """Differenz zwischen Hoch und Tief."""
        return round(self.hoch() - self.tief(), 2)

    # --- Zeitreihe: gleitender Durchschnitt ---
    def sma(self, fenster):
        """Simple Moving Average: Liste von (date, schnitt)-Paaren."""
        kurse = self._closes()
        ergebnis = []
        for i in range(len(kurse) - fenster + 1):
            ausschnitt = kurse[i:i + fenster]
            schnitt = round(sum(ausschnitt) / fenster, 2)
            ergebnis.append((self.daten[i + fenster - 1]["date"], schnitt))
        return ergebnis


# ===========================================================================
# Selbsttest – läuft nur bei direktem Start (python3 kursreihe.py)
# ===========================================================================
if __name__ == "__main__":
    import os

    # robuster Pfad zur DB, egal von wo gestartet wird:
    hier = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(hier, "..", "materialien", "quotes.db")

    reihe = Kursreihe.aus_sql(db)
    print(reihe)                              # AAPL: 2517 Tage (2010-06-03 bis 2020-06-02)
    print("repr:        ", repr(reihe))
    print("Tage (len):  ", len(reihe))
    print("erster Tag:  ", reihe[0])          # __getitem__
    print("letzter Tag: ", reihe[-1])
    print("hoch / tief: ", reihe.hoch(), reihe.tief())
    print("spanne:      ", reihe.spanne)      # @property, ohne Klammern
    print("mittel:      ", reihe.mittel())
    print("gesamtrendite:", reihe.gesamtrendite(), "%")

    # Teilbereich als eigene Kursreihe:
    corona = reihe.zeitraum("2020-02-01", "2020-04-30")
    print(corona)
    print("  Rendite im Zeitraum:", corona.gesamtrendite(), "%")

    # SMA: letzte 3 Werte des 20-Tage-Schnitts
    print("SMA(20) Ende:", reihe.sma(20)[-3:])
