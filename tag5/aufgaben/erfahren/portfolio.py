# Aufgabe (erfahren): Ein Portfolio aus mehreren Wertpapieren
#
# Baut auf wertpapier_oop.py auf und zeigt KOMPOSITION ("hat ein"):
# Ein Portfolio HAT mehrere Wertpapier-Objekte. Es erbt NICHT von Wertpapier –
# es enthält welche.
#
# Voraussetzung: deine Klasse Wertpapier aus wertpapier_oop.py funktioniert.
#
# ---------------------------------------------------------------------------
# AUFGABE: Baue die Klasse Portfolio aus. Sie verwaltet eine Liste von
# Wertpapier-Objekten und bietet Auswertungen über alle hinweg.
# ---------------------------------------------------------------------------
from wertpapier_oop import Wertpapier, DB


class Portfolio:
    def __init__(self, name):
        # TODO: name speichern, leere Liste self.papiere anlegen
        #       (eigene Liste pro Objekt – nicht als Klassenattribut!).
        self.name = name
        self.papiere = []

    def hinzufuegen(self, wertpapier):
        # TODO: ein Wertpapier-Objekt an self.papiere anhängen.
        pass

    def __len__(self):
        # TODO: Anzahl der enthaltenen Wertpapiere.
        pass

    def __iter__(self):
        # TODO: über die Wertpapiere iterierbar machen (Tipp: return iter(...)).
        #       Dann funktioniert: for wp in portfolio: ...
        pass

    def bestes_papier(self):
        # TODO: das Wertpapier mit der höchsten gesamtrendite() zurückgeben.
        #       Tipp: max(self.papiere, key=lambda wp: wp.gesamtrendite())
        pass

    def durchschnittsrendite(self):
        # TODO: Mittelwert der gesamtrendite() aller Papiere, auf 2 Stellen.
        #       Leeres Portfolio -> 0.0.
        pass

    def __str__(self):
        # TODO: z. B. "Portfolio 'Tech': 3 Papiere"
        pass


# --- Test (einkommentieren, wenn beide Klassen stehen) ---
# Hinweis: Mangels weiterer Tabellen laden wir hier dasselbe Symbol mehrfach –
# es geht ums Zusammenspiel der Objekte, nicht um echte Diversifikation.
# if __name__ == "__main__":
#     p = Portfolio("Demo")
#     p.hinzufuegen(Wertpapier.aus_sql(DB, "AAPL"))
#     p.hinzufuegen(Wertpapier.aus_sql(DB, "AAPL-Kopie"))
#     print(p)                        # Portfolio 'Demo': 2 Papiere
#     print("Anzahl:", len(p))
#     for wp in p:                    # nutzt __iter__
#         print("  ", wp)
#     print("bestes:", p.bestes_papier().symbol)
#     print("Schnitt-Rendite:", p.durchschnittsrendite(), "%")
