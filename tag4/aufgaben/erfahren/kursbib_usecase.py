# Use-Case (erfahren): Anlage-Check mit der kursbib
#
# Szenario: Du hast am ERSTEN Handelstag der Kursreihe 10.000 € in die Aktie
# investiert. Werte mit deiner Bibliothek kursbib.py aus, wie sich das
# entwickelt hat – und wirf einen Blick auf den Trend.
#
# Voraussetzung: kursbib.py ist ausgefüllt und liegt daneben.
# Datenquelle: ../../../materialien/quotes.db  (oder die CSV)
#
# Dieses Skript ist als ANWENDUNG gedacht: der untere Teil ist fertig, sobald
# deine Bib funktioniert. Du musst hier nichts mehr ausfüllen – nur laufen
# lassen und das Ergebnis verstehen. (Wenn etwas crasht: erst die Bib fixen.)

import os
import kursbib as kb

HIER = os.path.dirname(__file__)
DB = os.path.join(HIER, "..", "..", "..", "materialien", "quotes.db")
CSV = os.path.join(HIER, "..", "..", "..", "materialien", "HistoricalQuotes.csv")

START_KAPITAL = 10_000.0


def main():
    # Laden – wahlweise SQL oder CSV (beide liefern dasselbe)
    daten = kb.load("sql", DB)
    print(f"{len(daten)} Handelstage: {daten[0]['date']} bis {daten[-1]['date']}")
    print("-" * 50)

    # Kennzahlen über den gesamten Zeitraum
    print(f"Höchstkurs:        {kb.hoch(daten):.2f}")
    print(f"Tiefstkurs:        {kb.tief(daten):.2f}")
    print(f"Durchschnittskurs: {kb.mittel(daten):.2f}")

    # Die Anlage-Rechnung
    rend = kb.gesamtrendite(daten)
    endwert = START_KAPITAL * (1 + rend / 100)
    print("-" * 50)
    print(f"Investiert am {daten[0]['date']}: {START_KAPITAL:,.0f} €")
    print(f"Gesamtrendite:    {rend:.2f} %")
    print(f"Wert am {daten[-1]['date']}: {endwert:,.0f} €")

    # Der beste Tag
    top = kb.bester_tag(daten)
    print("-" * 50)
    print(f"Bester Tag: {top['date']} mit Schlusskurs {top['close']:.2f}")

    # Trend-Check: liegt der letzte Kurs über dem 200-Tage-Schnitt?
    # (Klassisches, einfaches Signal: Kurs > SMA200 -> Aufwärtstrend.)
    sma200 = kb.sma(daten, 200)
    letzter_kurs = daten[-1]["close"]
    letzter_sma = sma200[-1][1]          # (date, schnitt) -> schnitt
    trend = "Aufwärtstrend" if letzter_kurs > letzter_sma else "Abwärtstrend"
    print("-" * 50)
    print(f"Letzter Kurs:  {letzter_kurs:.2f}")
    print(f"SMA200:        {letzter_sma:.2f}")
    print(f"Einschätzung:  {trend}")


if __name__ == "__main__":
    main()
