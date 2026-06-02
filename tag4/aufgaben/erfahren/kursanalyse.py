# Aufgabe (erfahren): Kursanalyse mit der Bib data_source
#
# Nutze die fertige Bibliothek data_source.py (liegt in tag4/) für eine
# eigene Kursanalyse. Die Bib kann CSV UND SQLite lesen – probiere beides.
#
# Datenquellen (relativ zu diesem Skript):
#   CSV:  ../../../materialien/HistoricalQuotes.csv
#   SQL:  ../../../materialien/quotes.db
#
# Damit der Import von data_source klappt, muss Python das tag4/-Verzeichnis
# finden. Einfachster Weg für die Übung: die Zeile mit sys.path unten (fertig).
#
# ---------------------------------------------------------------------------
# AUFGABE:
#   1. Lade die Daten EINMAL aus CSV und EINMAL aus SQL.
#      Prüfe: liefern beide gleich viele Tage?
#   2. Gib für die Gesamtreihe aus: Hoch, Tief, Mittel, Gesamtrendite.
#   3. Schränke mit ds.zeitraum(...) auf EIN Jahr ein (z.B. 2019) und
#      wiederhole die Kennzahlen nur für dieses Jahr.
#   4. Ermittle den besten Tag und den größten Tagesgewinn.
#   5. Berechne den 50-Tage-SMA und gib die letzten 5 Werte aus.
#
# Kür: Finde alle Tage mit einem Tagesgewinn über 5 % (Filter über
#      ds.tagesveraenderung(...)).
# ---------------------------------------------------------------------------

import sys
import os

# tag4/ in den Suchpfad legen, damit "import data_source" funktioniert
# (von hier aus drei Ebenen hoch: erfahren -> aufgaben -> tag4)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tag4"))

import data_source as ds

CSV = os.path.join(os.path.dirname(__file__), "..", "..", "..", "materialien", "HistoricalQuotes.csv")
DB  = os.path.join(os.path.dirname(__file__), "..", "..", "..", "materialien", "quotes.db")

# 1) Laden
# daten_csv = ds.load("csv", CSV)
# daten_sql = ds.load("sql", DB)
# print("CSV:", len(daten_csv), "| SQL:", len(daten_sql))

# 2) Kennzahlen Gesamtreihe
# print("Hoch:", ds.hoch(daten_csv))
# ...

# 3) Nur ein Jahr
# jahr_2019 = ds.zeitraum(daten_csv, "2019-01-01", "2019-12-31")
# print("2019 – Mittel:", ds.mittel(jahr_2019))
# ...

# 4) Bester Tag / größter Tagesgewinn
# ...

# 5) SMA50 (letzte 5)
# ...

# Kür: Tage mit > 5 % Gewinn
# starke = [(d, v) for d, v in ds.tagesveraenderung(daten_csv) if v > 5]
# print("Tage über 5 %:", len(starke))
