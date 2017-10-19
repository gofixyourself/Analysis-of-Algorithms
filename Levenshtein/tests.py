import standard_levenshtein as standard
import modified_levenshtein as modified
import levenshtein_with_recursion as recursion
import unittest


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


class TestsForModifiedLevenshtein(unittest.TestCase):
    def test_first(self):
        self.assertEqual(modified.modified_levenstein("ABC", "ABC"), 0)

    def test_second(self):
        self.assertEqual(modified.modified_levenstein("ABC", "ABCDEF"), 3)

    def test_third(self):
        self.assertEqual(modified.modified_levenstein("ABC", "BCDE"), 3)

    def test_fourth(self):
        self.assertEqual(modified.modified_levenstein("BCDE", "ABCDEF"), 2)

    def test_fiveth(self):
        self.assertEqual(modified.modified_levenstein("AAAAB", "BAAAA"), 2)

    def test_sixth(self):
        self.assertEqual(modified.modified_levenstein("Me", "mE"), 2)


class TestsForRecursionLevenshtein(unittest.TestCase):
    def test_first(self):
        self.assertEqual(recursion.levenshtein_disctance_recursion("ABC", "ABC"), 0)

    def test_second(self):
        self.assertEqual(recursion.levenshtein_disctance_recursion("ABC", "ABCDEF"), 3)

    def test_third(self):
        self.assertEqual(recursion.levenshtein_disctance_recursion("BCDE", "ABC"), 4)

    def test_fourth(self):
        self.assertEqual(recursion.levenshtein_disctance_recursion("BCDE", "ABCDEF"), 3)

    def test_fiveth(self):
        self.assertEqual(recursion.levenshtein_disctance_recursion("AAAAB", "BAAAA"), 2)

    def test_sixth(self):
        self.assertEqual(recursion.levenshtein_disctance_recursion("Me", "mE"), 2)


if __name__ == '__main__':
    unittest.main()
