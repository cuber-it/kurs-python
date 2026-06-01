# quotes_to_sqlite.py
# Liest HistoricalQuotes.csv ein und schreibt die Kurse in eine SQLite-DB.
#
# Demonstriert die Brücke: CSV -> Python-Datenstrukturen -> SQLite.
# Stolperfallen im CSV, die wir unterwegs bereinigen:
#   - Header und Werte haben Leerzeichen nach dem Komma
#   - Preise stehen als "$323.34"  -> Dollarzeichen muss weg
#   - Datum im US-Format MM/DD/YYYY -> wir normalisieren auf YYYY-MM-DD (sortierbar)

import csv
import sqlite3
from datetime import datetime

CSV_DATEI = r"/home/ucuber/Workspace/kurse/kurs-python/materialien/HistoricalQuotes.csv"
DB_DATEI = "quotes.db"


def preis(text):
    """'$323.34' -> 323.34"""
    return float(text.strip().lstrip("$"))


def datum(text):
    """'06/02/2020' -> '2020-06-02'"""
    return datetime.strptime(text.strip(), "%m/%d/%Y").strftime("%Y-%m-%d")


def lies_csv(pfad):
    """CSV einlesen und als Liste von Dicts zurückgeben (bereinigt)."""
    zeilen = []
    with open(pfad, newline="", encoding="utf-8") as f:
        leser = csv.DictReader(f, skipinitialspace=True)  # frisst Leerzeichen nach Komma
        for r in leser:
            zeilen.append({
                "date": datum(r["Date"]),
                "close": preis(r["Close/Last"]),
                "volume": int(r["Volume"].strip()),
                "open": preis(r["Open"]),
                "high": preis(r["High"]),
                "low": preis(r["Low"]),
            })
    return zeilen


def schreib_sqlite(zeilen, db_pfad):
    """Tabelle anlegen und alle Zeilen einfügen."""
    con = sqlite3.connect(db_pfad)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS quotes")
    cur.execute("""
        CREATE TABLE quotes (
            date   TEXT PRIMARY KEY,
            close  REAL,
            volume INTEGER,
            open   REAL,
            high   REAL,
            low    REAL
        )
    """)
    # executemany ist schneller als viele einzelne INSERTs
    cur.executemany(
        "INSERT INTO quotes VALUES (:date, :close, :volume, :open, :high, :low)",
        zeilen,
    )
    con.commit()
    con.close()


def main():
    zeilen = lies_csv(CSV_DATEI)
    print(f"{len(zeilen)} Zeilen aus {CSV_DATEI} gelesen.")

    schreib_sqlite(zeilen, DB_DATEI)
    print(f"In {DB_DATEI} geschrieben.")

    # Smoke-Test: ein paar Zeilen wieder auslesen
    con = sqlite3.connect(DB_DATEI)
    cur = con.cursor()
    anzahl = cur.execute("SELECT COUNT(*) FROM quotes").fetchone()[0]
    print(f"Kontrolle: {anzahl} Zeilen in der DB.")
    print("Neueste 3:")
    for row in cur.execute("SELECT date, close FROM quotes ORDER BY date DESC LIMIT 3"):
        print(f"  {row[0]}: {row[1]} $")
    con.close()


if __name__ == "__main__":
    main()
