import unittest

from src.factors import findFactors

IGNORE_TESTS = False


class TestFindFactors(unittest.TestCase):

    def test_prime(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(findFactors(7), {7: 1})

    def test_composite(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(findFactors(12), {2: 2, 3: 1})

    def test_power_of_two(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(findFactors(8), {2: 3})

    def test_large(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(findFactors(360), {2: 3, 3: 2, 5: 1})

    def test_one(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(findFactors(1), {})

    def test_zero(self):
        if IGNORE_TESTS:
            return
        self.assertEqual(findFactors(0), {})


if __name__ == "__main__":
    unittest.main()
