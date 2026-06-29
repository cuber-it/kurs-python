import unittest
from rechteck import Rechteck


class TestRechteck(unittest.TestCase):

    def setUp(self):
        # läuft vor JEDER Testmethode -> frische Objekte
        self.r = Rechteck(4, 3)
        self.q = Rechteck(5, 5)

    def test_attribute(self):
        self.assertEqual(self.r.breite, 4)
        self.assertEqual(self.r.hoehe, 3)

    def test_flaeche(self):
        self.assertEqual(self.r.flaeche(), 12)
        self.assertEqual(self.q.flaeche(), 25)

    def test_umfang(self):
        self.assertEqual(self.r.umfang(), 14)
        self.assertEqual(self.q.umfang(), 20)

    def test_ist_quadrat(self):
        self.assertFalse(self.r.ist_quadrat())
        self.assertTrue(self.q.ist_quadrat())

    def test_str(self):
        self.assertEqual(str(self.r), "Rechteck 4x3")

    def test_unabhaengige_objekte(self):
        # ein Objekt ändern darf das andere nicht beeinflussen
        self.r.breite = 10
        self.assertEqual(self.q.breite, 5)


if __name__ == "__main__":
    unittest.main()
