# Aufgabe (erfahren): Wertpapier als KLASSE
#
# An Tag 4 war die Kursanalyse FUNKTIONAL: load_sql(...) lieferte eine Liste
# von Dicts, die du durch Funktionen wie mittel(daten), hoch(daten) gereicht
# hast. Jetzt das GLEICHE objektorientiert – Daten und Verhalten in einem Objekt.
#
# Vergleiche bewusst mit tag4/data_source.py und tag5/kursreihe.py.
#
# Datenformat (wie gehabt): Liste von Dicts, je Handelstag, nach Datum sortiert:
#   [{"date": "2010-06-03", "close": 37.59, "volume": 162341809}, ...]
#
# ---------------------------------------------------------------------------
# AUFGABE: Baue die Klasse Wertpapier aus. Stubs (pass / return) ersetzen.
# Denke an Sonderfälle (leere Liste, Division durch 0). Docstrings schreiben.
# ---------------------------------------------------------------------------
import os
import sqlite3

DB = os.path.join(os.path.dirname(__file__), "..", "..", "..", "materialien", "quotes.db")


class Wertpapier:
    def __init__(self, symbol, daten):
        # TODO: symbol und daten als Attribute speichern.
        #       daten sicherheitshalber nach "date" sortieren.
        self.symbol = symbol
        self.daten = daten

    @classmethod
    def aus_sql(cls, db_pfad, symbol="AAPL"):
        """Alternativer Konstruktor: lädt die Kursdaten aus der SQLite-DB
        (Tabelle quotes) und gibt ein fertiges Wertpapier-Objekt zurück."""
        # TODO: Verbindung öffnen, "SELECT date, close, volume FROM quotes
        #       ORDER BY date ASC" ausführen, Ergebnis in Liste von Dicts wandeln,
        #       Verbindung schließen und cls(symbol, daten) zurückgeben.
        pass

    def _closes(self):
        # TODO: Liste der Schlusskurse zurückgeben (List Comprehension).
        return []

    def hoch(self):
        # TODO: höchster Schlusskurs
        pass

    def tief(self):
        # TODO: niedrigster Schlusskurs
        pass

    def mittel(self):
        # TODO: Durchschnitt, auf 2 Stellen gerundet; leere Liste -> 0.0
        pass

    def gesamtrendite(self):
        # TODO: (letzter - erster) / erster * 100, gerundet; < 2 Tage -> 0.0
        pass

    def __len__(self):
        # TODO: Anzahl Handelstage
        pass

    def __str__(self):
        # TODO: z. B. "AAPL: 2517 Tage, Mittel 121.19 EUR"
        pass


# --- Test (einkommentieren, wenn die Klasse steht) ---
# if __name__ == "__main__":
#     wp = Wertpapier.aus_sql(DB)
#     print(wp)                      # AAPL: 2517 Tage, Mittel 121.19 EUR
#     print("Tage:", len(wp))        # 2517
#     print("Hoch/Tief:", wp.hoch(), wp.tief())
#     print("Gesamtrendite:", wp.gesamtrendite(), "%")
