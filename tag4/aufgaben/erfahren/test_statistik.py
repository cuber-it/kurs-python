# Aufgabe (erfahren): Eigene Unittests schreiben
#
# Schreibe Tests für die statistik()-Funktion aus statistik.py.
# (Setzt voraus, dass du statistik.py vorher fertiggestellt hast.)
#
# AUSFÜHREN:
#   python3 -m unittest -v test_statistik.py
#
# Schreibe mindestens diese Testfälle:
#   1. statistik(7, 2, 9, 4)  -> min=2, max=9, schnitt=5.5
#   2. eine einzelne Zahl     -> min=max=schnitt
#   3. der leere Aufruf       -> dein definierter Sonderfall
#
# Tipps:
#   - mehrere Rückgabewerte: erg = statistik(...); dann erg[0], erg[1], erg[2]
#     ODER direkt entpacken: mini, maxi, schnitt = statistik(...)
#   - assertEqual für die Vergleiche
#   - bei Durchschnitt ggf. assertAlmostEqual (Fließkomma!)

import unittest
from statistik import statistik


class TestStatistik(unittest.TestCase):

    def test_mehrere_zahlen(self):
        mini, maxi, schnitt = statistik(7, 2, 9, 4)
        # self.assertEqual(mini, 2)
        # self.assertEqual(maxi, 9)
        # self.assertAlmostEqual(schnitt, 5.5)
        pass

    def test_eine_zahl(self):
        # eine einzelne Zahl: min == max == schnitt
        pass

    def test_leer(self):
        # der von dir definierte Sonderfall für statistik()
        pass


if __name__ == "__main__":
    unittest.main()
