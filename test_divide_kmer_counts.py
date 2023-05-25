import unittest

from divide_kmer_counts import divide_kmer_counts


class TestDivideKmerCountsFunction(unittest.TestCase):
    def test_that_a_new_dict_is_returned(self):
        counts = { 'T': 4, 'A': 56, 'G': 2 }
        divided = divide_kmer_counts(counts, 1)
        self.assertTrue(divided == counts)
        # a new dict was returned
        self.assertFalse(divided is counts)

    def test_empty_kmer_counts_dict(self):
        divided = divide_kmer_counts({}, 3)
        self.assertEqual(divided, {})

    def test_kmer_counts_dict_with_only_one_count(self):
        counts = { 'AAA': 8 }
        divided = divide_kmer_counts(counts, 3)
        self.assertEqual(divided, { 'AAA': 8 / 3 })

    def test_kmer_counts_dict_with_multiple_counts(self):
        counts = { 'A': 5, 'AA': 27, 'AAA': 88 }
        divided = divide_kmer_counts(counts, 8)
        self.assertEqual(divided, { 'A': 5 / 8, 'AA': 27 / 8, 'AAA': 88 / 8 })

    def test_negative_counts_and_a_negative_factor(self):
        counts = { 'a': 2, 'b': -29, 'c': 0 }
        divided = divide_kmer_counts(counts, -6)
        self.assertEqual(divided, { 'a': 2 / -6, 'b': -29 / -6, 'c': 0 })
