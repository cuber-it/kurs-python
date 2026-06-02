# Aufgabe (erfahren): Wertpapier-Bibliothek "wertpapier.py"
#
# Baue eine kleine, wiederverwendbare Funktionssammlung (eine "Bib") rund um
# Aktienkurse. Die Funktionen sollen allgemein sein, also mit übergebenen
# Daten arbeiten – NICHT selbst auf die Datenbank zugreifen. Das Laden der
# Daten passiert im Nutzer-Skript analyse.py.
#
# Datenformat (so liefert es analyse.py): eine Liste von Dicts, je ein
# Handelstag, aufsteigend nach Datum sortiert:
#   [{"date": "2010-06-03", "close": 37.58}, {"date": "2010-06-04", ...}, ...]
#
# ---------------------------------------------------------------------------
# AUFGABE: Fülle die folgenden Funktionen aus. Jede gibt etwas ZURÜCK (return).
# Schreibe Docstrings. Denke an Sonderfälle (leere Liste, Division durch 0).
# ---------------------------------------------------------------------------

def import_daten(source, type):
    pass

def schlusskurse(daten):
    """Liste nur der Schlusskurse (close) aus den Datensätzen."""
    # Tipp: List Comprehension über daten -> d["close"]
    pass


def rendite(kurs_alt, kurs_neu):
    """Prozentuale Rendite von kurs_alt auf kurs_neu.
    Beispiel: rendite(100, 110) -> 10.0
    """
    # Tipp: (neu - alt) / alt * 100 ; Sonderfall alt == 0 abfangen
    pass


def hoechstkurs(daten):
    """Höchsten Schlusskurs zurückgeben (Tipp: max über schlusskurse)."""
    pass


def tiefstkurs(daten):
    """Niedrigsten Schlusskurs zurückgeben."""
    pass


def durchschnitt(daten):
    """Durchschnittlicher Schlusskurs, auf 2 Stellen gerundet."""
    # Tipp: sum(...) / len(...) ; leere Liste abfangen
    pass


def gleitender_durchschnitt(daten, fenster):
    """Liste der gleitenden Durchschnitte über 'fenster' Tage (SMA).
    Für die ersten (fenster-1) Tage gibt es noch keinen Wert.
    Ergebnislänge = len(daten) - fenster + 1
    """
    # Tipp: über die Schlusskurse slicen: kurse[i:i+fenster], davon der Schnitt
    pass


def bester_tag(daten):
    """Dict des Tages mit dem höchsten Schlusskurs (mit date + close).
    Tipp: max(daten, key=lambda d: d["close"])
    """
    pass


# Selbsttest – läuft nur bei direktem Start (python3 wertpapier.py)
if __name__ == "__main__":
    test = import_daten(
        [{"date": "2024-01-01", "close": 100.0},
         {"date": "2024-01-02", "close": 110.0},
         {"date": "2024-01-03", "close": 105.0},
        ],
        "liste"
    )
    print("schlusskurse:", schlusskurse(test))      # [100.0, 110.0, 105.0]
    print("rendite 100->110:", rendite(100, 110))   # 10.0
    print("hoch/tief:", hoechstkurs(test), tiefstkurs(test))  # 110.0 100.0
    print("durchschnitt:", durchschnitt(test))      # 105.0
    print("SMA(2):", gleitender_durchschnitt(test, 2))  # [105.0, 107.5]
    print("bester Tag:", bester_tag(test))          # {'date': '2024-01-02', ...}
