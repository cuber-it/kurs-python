# Tag 4 – Unittests mit dem Modul "unittest"
#
# Automatische Tests prüfen, ob Funktionen das tun, was sie sollen –
# auf Knopfdruck und immer wieder (z.B. nach jeder Änderung).
# unittest ist in der Standardbibliothek (kein pip nötig).
#
# Wir testen die Funktionen aus rechner.py (liegt daneben).
#
# AUSFÜHREN:
#   python3 -m unittest 09_unittests.py      (oder: python3 09_unittests.py)
#   python3 -m unittest -v 09_unittests.py   (-v = ausführlich)

import unittest
from rechner import addiere, teile, ist_gerade


# Eine Testklasse erbt von unittest.TestCase.
# Jede Methode, die mit "test_" beginnt, ist ein eigener Test.
class TestRechner(unittest.TestCase):

    def test_addiere_positiv(self):
        self.assertEqual(addiere(2, 3), 5)

    def test_addiere_negativ(self):
        self.assertEqual(addiere(-1, -1), -2)

    def test_teile_normal(self):
        self.assertEqual(teile(10, 2), 5)

    def test_teile_durch_null(self):
        # Prüfen, dass die richtige Ausnahme FLIEGT:
        with self.assertRaises(ValueError):
            teile(5, 0)

    def test_ist_gerade(self):
        self.assertTrue(ist_gerade(4))      # erwartet True
        self.assertFalse(ist_gerade(7))     # erwartet False


# Die wichtigsten assert-Methoden (Spickzettel):
#   assertEqual(a, b)        a == b
#   assertNotEqual(a, b)     a != b
#   assertTrue(x) / assertFalse(x)
#   assertIn(x, sammlung)    x in sammlung
#   assertRaises(Fehler)     erwartet eine Ausnahme
#   assertAlmostEqual(a, b)  für Fließkomma (Rundungsfehler!)


# Damit das Skript auch mit "python3 09_unittests.py" läuft:
if __name__ == "__main__":
    unittest.main()
