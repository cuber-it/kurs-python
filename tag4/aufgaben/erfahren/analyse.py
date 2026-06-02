# Aufgabe (erfahren): Analyse-Skript – nutzt die Bib "wertpapier.py"
#
# Dieses Skript LÄDT die Kursdaten aus der SQLite-DB und wertet sie mit
# den Funktionen aus deiner Bibliothek wertpapier.py aus.
#
# Voraussetzung: materialien/quotes.db existiert (siehe Tag 3 / quotes_to_sqlite).
#
# AUFGABE:
#   1. Daten aus der DB laden (Code unten ist fertig – verstehen!).
#   2. Deine Bib-Funktionen aufrufen und die Ergebnisse ausgeben.
#   3. Beantworte mit der Bib:
#        - Höchst- und Tiefstkurs im Zeitraum
#        - Durchschnittskurs
#        - Gesamtrendite vom ersten bis zum letzten Tag
#        - bester Tag (höchster Schlusskurs) mit Datum
#        - die letzten 5 Werte des 50-Tage-Durchschnitts (SMA 50)

import sqlite3
import wertpapier as wp

DB = "../../../materialien/quotes.db"   # relativ zu diesem Skript

# --- Daten laden: DB -> Liste von Dicts (fertig vorgegeben) ---
def lade_kurse(db_pfad):
    con = sqlite3.connect(db_pfad)
    con.row_factory = sqlite3.Row          # Zugriff per Spaltenname
    cur = con.cursor()
    cur.execute("SELECT date, close FROM quotes ORDER BY date ASC")
    daten = [{"date": r["date"], "close": r["close"]} for r in cur.fetchall()]
    con.close()
    return daten

daten = lade_kurse(DB)
print(f"{len(daten)} Handelstage geladen "
      f"({daten[0]['date']} bis {daten[-1]['date']})")

# --- AB HIER: deine Auswertung mit der Bib ---
# Tipp – Gesamtrendite:
#   erster = daten[0]["close"]
#   letzter = daten[-1]["close"]
#   print("Gesamtrendite:", wp.rendite(erster, letzter), "%")
#
# print("Höchstkurs:", wp.hoechstkurs(daten))
# print("Tiefstkurs:", wp.tiefstkurs(daten))
# print("Durchschnitt:", wp.durchschnitt(daten))
# print("Bester Tag:", wp.bester_tag(daten))
# print("SMA50 (letzte 5):", wp.gleitender_durchschnitt(daten, 50)[-5:])
