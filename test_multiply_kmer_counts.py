import unittest

from multiply_kmer_counts import multiply_kmer_counts


class TestMultiplyKmerCountsFunction(unittest.TestCase):
    def test_that_a_new_dict_is_returned(self):
        counts = { 'AC': 2, 'GGG': 24 }
        multiplied = multiply_kmer_counts(counts, 1)
        self.assertTrue(multiplied == counts)
        # a new dict was returned
        self.assertFalse(multiplied is counts)

    def test_empty_kmer_counts_dict(self):
        multiplied = multiply_kmer_counts({}, 2)
        self.assertEqual(multiplied, {})

    def test_kmer_counts_dict_with_one_count(self):
        counts = { 'AT': 5 }
        multiplied = multiply_kmer_counts(counts, 3)
        self.assertEqual(multiplied, { 'AT': 15 })

    def test_kmer_counts_dict_with_multiple_counts(self):
        counts = { 'A': 2, 'ACA': 10, 'GG': 12 }
        multiplied = multiply_kmer_counts(counts, 4)
        self.assertEqual(multiplied, { 'A': 8, 'ACA': 40, 'GG': 48 })

    def test_negative_counts_and_negative_factor(self):
        counts = { 'A': -3, 'G': 5, 'CC': -12 }
        multiplied = multiply_kmer_counts(counts, -6)
        self.assertEqual(multiplied, { 'A': 18, 'G': -30, 'CC': 72 })

    def test_factor_of_zero(self):
        counts = { 'AA': 88, 'C': -16, 'GT': 0 }
        multiplied = multiply_kmer_counts(counts, 0)
        self.assertEqual(multiplied, { 'AA': 0, 'C': 0, 'GT': 0 })
