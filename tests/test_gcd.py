import unittest

from src.gcd import greatestCommonDivisor

IGNORE_TESTS = False


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_common_case(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(greatestCommonDivisor(12, 8), 4)

    def test_coprime(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(greatestCommonDivisor(7, 13), 1)

    def test_one_is_zero(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(greatestCommonDivisor(5, 0), 5)

    def test_both_zero(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(greatestCommonDivisor(0, 0), 0)

    def test_same_values(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(greatestCommonDivisor(9, 9), 9)

    def test_large(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(greatestCommonDivisor(100, 75), 25)


if __name__ == "__main__":
    unittest.main()
