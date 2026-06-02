# Aufgabe (erfahren): Eigene Unittests schreiben
#
# Schreibe Tests für die statistik()-Funktion aus statistik.py.
# (Setzt voraus, dass du statistik.py vorher fertiggestellt hast.)
#
# AUSFÜHREN:
#   python3 -m unittest -v test_statistik.py
#
import unittest
import statistik as stat


class TestMinMaxSum(unittest.TestCase):

    def test_min_with_positive_numbers(self):
        self.assertEqual(stat.min(3, 1, 7, 2), 1)

    def test_min_with_negative_numbers(self):
        self.assertEqual(stat.min(-3, -1, -7, -2), -7)

    def test_min_with_single_value(self):
        self.assertEqual(stat.min(42), 42)

    def test_max_with_positive_numbers(self):
        self.assertEqual(stat.max(3, 1, 7, 2), 7)

    def test_max_with_negative_numbers(self):
        self.assertEqual(stat.max(-3, -1, -7, -2), -1)

    def test_max_with_single_value(self):
        self.assertEqual(stat.max(42), 42)

    def test_sum_with_positive_numbers(self):
        self.assertEqual(stat.sum(1, 2, 3, 4), 10)

    def test_sum_with_negative_numbers(self):
        self.assertEqual(stat.sum(-1, -2, -3), -6)

    def test_sum_with_mixed_numbers(self):
        self.assertEqual(stat.sum(-5, 10, -2), 3)

    def test_sum_with_single_value(self):
        self.assertEqual(stat.sum(42), 42)

    def test_sum_without_values(self):
        self.assertEqual(stat.sum(), 0)

    def test_min_without_values_raises_error(self):
        with self.assertRaises(IndexError):
            stat.min()

    def test_max_without_values_raises_error(self):
        with self.assertRaises(IndexError):
            stat.max()

    def test_mean_with_positive_numbers(self):
        self.assertEqual(stat.mean(1, 2, 3), 2)

    def test_mean_with_single_value(self):
        self.assertEqual(stat.mean(42), 42)

    def test_mean_with_negative_numbers(self):
        self.assertEqual(stat.mean(-1, -2, -3), -2)

    def test_mean_with_mixed_numbers(self):
        self.assertEqual(stat.mean(-1, 1), 0)

    def test_mean_with_float_result(self):
        self.assertAlmostEqual(stat.mean(1, 2), 1.5)

    def test_mean_with_zeroes(self):
        self.assertEqual(stat.mean(0, 0, 0), 0)

    def test_mean_without_values_raises_error(self):
        with self.assertRaises(ValueError):
            stat.mean()

if __name__ == "__main__":
    unittest.main()
