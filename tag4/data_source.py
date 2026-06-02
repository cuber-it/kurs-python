# Tag 4 – data_source.py  (Vorführ-Bibliothek, fertig & lauffähig)
#
# Eine kleine Datenquelle für Kursdaten – wahlweise aus CSV ODER SQLite,
# komplett mit der Standardbibliothek (KEIN pandas). Dazu typische
# Analyse- und Zeitreihen-Funktionen.
#
# Alles funktional gehalten: Funktionen geben Daten zurück, kein globaler
# Zustand, keine Klassen. Datenformat durchgängig: Liste von Dicts, je ein
# Handelstag, aufsteigend nach Datum:
#   [{"date": "2010-06-03", "close": 37.58, "volume": 162341809}, ...]

import csv
import sqlite3
from datetime import datetime


# ===========================================================================
# 1) LADEN – zwei Quellen, gleiches Ausgabeformat
# ===========================================================================

def _preis(text):
    """Hilfsfunktion: '$323.34' -> 323.34"""
    return float(text.strip().lstrip("$"))


def _datum(text):
    """Hilfsfunktion: '06/02/2020' -> '2020-06-02' (sortierbar)"""
    return datetime.strptime(text.strip(), "%m/%d/%Y").strftime("%Y-%m-%d")


def load_csv(pfad):
    """Kursdaten aus einer CSV-Datei lesen (Format der HistoricalQuotes.csv).
    Gibt eine nach Datum aufsteigend sortierte Liste von Dicts zurück.
    """
    daten = []
    with open(pfad, newline="", encoding="utf-8") as f:
        leser = csv.DictReader(f, skipinitialspace=True)
        for r in leser:
            daten.append({
                "date": _datum(r["Date"]),
                "close": _preis(r["Close/Last"]),
                "volume": int(r["Volume"].strip()),
            })
    daten.sort(key=lambda d: d["date"])          # CSV ist absteigend -> drehen
    return daten


def load_sql(db_pfad):
    """Kursdaten aus einer SQLite-DB lesen (Tabelle 'quotes').
    Gibt eine nach Datum aufsteigend sortierte Liste von Dicts zurück.
    """
    con = sqlite3.connect(db_pfad)
    con.row_factory = sqlite3.Row                # Zugriff per Spaltenname
    cur = con.cursor()
    cur.execute("SELECT date, close, volume FROM quotes ORDER BY date ASC")
    daten = [dict(date=r["date"], close=r["close"], volume=r["volume"])
             for r in cur.fetchall()]
    con.close()
    return daten


def load(quelle, pfad):
    """Bequemer Umschalter: quelle = 'csv' oder 'sql'."""
    if quelle == "csv":
        return load_csv(pfad)
    if quelle == "sql":
        return load_sql(pfad)
    raise ValueError(f"Unbekannte Quelle: {quelle!r} (erlaubt: 'csv', 'sql')")


# ===========================================================================
# 2) AUSWAHL / FILTER
# ===========================================================================

def closes(daten):
    """Nur die Schlusskurse als Liste."""
    return [d["close"] for d in daten]


def zeitraum(daten, von, bis):
    """Datensätze im Datumsbereich [von, bis] (Strings 'YYYY-MM-DD', inklusive)."""
    return [d for d in daten if von <= d["date"] <= bis]


# ===========================================================================
# 3) KENNZAHLEN
# ===========================================================================

def hoch(daten):
    """Höchster Schlusskurs."""
    return max(closes(daten))


def tief(daten):
    """Niedrigster Schlusskurs."""
    return min(closes(daten))


def mittel(daten):
    """Durchschnittlicher Schlusskurs, auf 2 Stellen gerundet."""
    werte = closes(daten)
    return round(sum(werte) / len(werte), 2) if werte else 0.0


def rendite(kurs_alt, kurs_neu):
    """Prozentuale Rendite. rendite(100, 110) -> 10.0"""
    if kurs_alt == 0:
        return 0.0
    return round((kurs_neu - kurs_alt) / kurs_alt * 100, 2)


def gesamtrendite(daten):
    """Rendite vom ersten bis zum letzten Tag der Reihe (in %)."""
    if len(daten) < 2:
        return 0.0
    return rendite(daten[0]["close"], daten[-1]["close"])


# ===========================================================================
# 4) ZEITREIHEN
# ===========================================================================

def sma(daten, fenster):
    """Simple Moving Average: Liste der gleitenden Durchschnitte über
    'fenster' Tage. Ergebnislänge = len(daten) - fenster + 1.
    Gibt je (date, schnitt)-Paare zurück (Datum = letzter Tag des Fensters).
    """
    kurse = closes(daten)
    ergebnis = []
    for i in range(len(kurse) - fenster + 1):
        ausschnitt = kurse[i:i + fenster]
        schnitt = round(sum(ausschnitt) / fenster, 2)
        ergebnis.append((daten[i + fenster - 1]["date"], schnitt))
    return ergebnis


def tagesveraenderung(daten):
    """Tägliche prozentuale Veränderung gegenüber dem Vortag.
    Gibt je (date, veraenderung_prozent)-Paare zurück (ab dem 2. Tag).
    """
    ergebnis = []
    for i in range(1, len(daten)):
        v = rendite(daten[i - 1]["close"], daten[i]["close"])
        ergebnis.append((daten[i]["date"], v))
    return ergebnis


def bester_tag(daten):
    """Datensatz mit dem höchsten Schlusskurs."""
    return max(daten, key=lambda d: d["close"])


def groesster_tagesgewinn(daten):
    """(date, prozent) des Tages mit der höchsten Tagesveränderung."""
    veraenderungen = tagesveraenderung(daten)
    return max(veraenderungen, key=lambda paar: paar[1])


# ===========================================================================
# Selbsttest – läuft nur bei direktem Start (python3 data_source.py)
# ===========================================================================
if __name__ == "__main__":
    test = [
        {"date": "2024-01-01", "close": 100.0, "volume": 1000},
        {"date": "2024-01-02", "close": 110.0, "volume": 1200},
        {"date": "2024-01-03", "close": 99.0,  "volume": 900},
        {"date": "2024-01-04", "close": 105.0, "volume": 1100},
    ]
    print("closes:        ", closes(test))
    print("hoch / tief:   ", hoch(test), tief(test))
    print("mittel:        ", mittel(test))
    print("gesamtrendite: ", gesamtrendite(test), "%")
    print("SMA(2):        ", sma(test, 2))
    print("tagesveränd.:  ", tagesveraenderung(test))
    print("bester Tag:    ", bester_tag(test))
    print("max Tagesgewinn:", groesster_tagesgewinn(test))
