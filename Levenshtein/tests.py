import standard_levenshtein as standard
import modified_levenshtein as modified
import levenshtein_with_recursion as recursion
import unittest
import time


class TestsForStandardLevenshtein(unittest.TestCase):
    def test_first(self):
        self.assertEqual(standard.levenshtein_distance("ABC", "ABC"), 0)

    def test_second(self):
        self.assertEqual(standard.levenshtein_distance("ABC", "ABCDEF"), 3)

    def test_third(self):
        self.assertEqual(standard.levenshtein_distance("ABC", "BCDE"), 3)

    def test_fourth(self):
        self.assertEqual(standard.levenshtein_distance("BCDE", "ABCDEF"), 2)

    def test_fiveth(self):
        self.assertEqual(standard.levenshtein_distance("AAAAB", "BAAAA"), 2)

    def test_sixth(self):
        self.assertEqual(standard.levenshtein_distance("Me", "mE"), 2)


if __name__ == '__main__':
    unittest.main()
