# Aufgabe (erfahren): Kurs-Bibliothek "kursbib.py" – Funktions-Stubs ausfüllen
#
# Eine wiederverwendbare Funktionssammlung für Aktienkurse, wahlweise aus
# CSV oder SQLite – nur Standardbibliothek, KEIN pandas, KEINE Klassen.
#
# Datenformat durchgängig: Liste von Dicts, je ein Handelstag, aufsteigend
# nach Datum:
#   [{"date": "2010-06-03", "close": 37.58, "volume": 162341809}, ...]
#
# Die beiden String-Helfer (_preis, _datum) sind fertig – damit du dich
# auf die eigentliche Logik konzentrieren kannst. Alle Funktionen mit
# "pass" sind DEINE Aufgabe. Erst danach läuft kursbib_usecase.py.

import csv
import sqlite3
from datetime import datetime


# --- fertige Helfer (Datenbereinigung) ---
def _preis(text):
    """'$323.34' -> 323.34"""
    return float(text.strip().lstrip("$"))

def _datum(text):
    """'06/02/2020' -> '2020-06-02' (sortierbar)"""
    return datetime.strptime(text.strip(), "%m/%d/%Y").strftime("%Y-%m-%d")


# ===========================================================================
# LADEN
# ===========================================================================

def load_csv(pfad):
    """CSV (Format HistoricalQuotes.csv) -> Liste von Dicts, nach date aufsteigend.
    Tipp: csv.DictReader(f, skipinitialspace=True); Spalten 'Date','Close/Last',
    'Volume' mit _datum/_preis/int bereinigen; am Ende nach 'date' sortieren
    (die CSV ist absteigend!).
    """
    pass

def load_sql(db_pfad):
    """SQLite (Tabelle 'quotes') -> Liste von Dicts, nach date aufsteigend.
    Tipp: SELECT date, close, volume FROM quotes ORDER BY date ASC
    """
    pass

def load(quelle, pfad):
    """Umschalter: quelle == 'csv' -> load_csv, 'sql' -> load_sql,
    sonst ValueError.
    """
    pass


# ===========================================================================
# AUSWAHL
# ===========================================================================

def closes(daten):
    """Liste nur der Schlusskurse."""
    pass

def zeitraum(daten, von, bis):
    """Datensätze mit von <= date <= bis (Strings 'YYYY-MM-DD', inklusive)."""
    pass


# ===========================================================================
# KENNZAHLEN
# ===========================================================================

def hoch(daten):
    """Höchster Schlusskurs."""
    pass

def tief(daten):
    """Niedrigster Schlusskurs."""
    pass

def mittel(daten):
    """Durchschnittlicher Schlusskurs, auf 2 Stellen gerundet (leere Liste -> 0.0)."""
    pass

def rendite(kurs_alt, kurs_neu):
    """Prozentuale Rendite, 2 Stellen. rendite(100, 110) -> 10.0.
    Sonderfall kurs_alt == 0 abfangen.
    """
    pass

def gesamtrendite(daten):
    """Rendite vom ersten bis zum letzten Tag der Reihe (in %)."""
    pass


# ===========================================================================
# ZEITREIHEN
# ===========================================================================

def sma(daten, fenster):
    """Simple Moving Average: Liste von (date, schnitt)-Paaren über 'fenster'
    Tage. date = letzter Tag des Fensters. Länge = len(daten) - fenster + 1.
    """
    pass

def bester_tag(daten):
    """Datensatz mit dem höchsten Schlusskurs (Tipp: max(..., key=...))."""
    pass


# --- Selbsttest (läuft erst, wenn die Funktionen gefüllt sind) ---
if __name__ == "__main__":
    test = [
        {"date": "2024-01-01", "close": 100.0, "volume": 1000},
        {"date": "2024-01-02", "close": 110.0, "volume": 1200},
        {"date": "2024-01-03", "close": 105.0, "volume": 900},
    ]
    print("closes:       ", closes(test))            # [100.0, 110.0, 105.0]
    print("hoch / tief:  ", hoch(test), tief(test))  # 110.0 100.0
    print("mittel:       ", mittel(test))            # 105.0
    print("gesamtrendite:", gesamtrendite(test))     # 5.0
    print("SMA(2):       ", sma(test, 2))            # [('2024-01-02',105.0),('2024-01-03',107.5)]
    print("bester Tag:   ", bester_tag(test))        # {'date':'2024-01-02',...}
