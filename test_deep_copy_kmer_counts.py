import unittest

from deep_copy_kmer_counts import deep_copy_kmer_counts


class TestDeepCopyKmerCountsFunction(unittest.TestCase):
    def test_that_a_copy_is_returned(self):
        counts = { 'AA': 2, 'GGT': 34 }
        dc = deep_copy_kmer_counts(counts)
        self.assertTrue(dc == counts)
        # is not the same dict
        self.assertFalse(dc is counts)

    def test_empty_kmer_counts_dict(self):
        dc = deep_copy_kmer_counts({})
        self.assertEqual(dc, {})

    def test_only_one_kmer_count(self):
        counts = { 'A': 57 }
        dc = deep_copy_kmer_counts(counts)
        self.assertEqual(dc, { 'A': 57 })

    def test_positive_and_negative_counts(self):
        counts = { 'GTGAC': 59, 'CC': -124 }
        dc = deep_copy_kmer_counts(counts)
        self.assertEqual(dc, { 'GTGAC': 59, 'CC': -124 })

    def test_counts_of_zero(self):
        counts = { 'GG': 0, 'C': 0, 'A': 0 }
        dc = deep_copy_kmer_counts(counts)
        self.assertEqual(dc, { 'GG': 0, 'C': 0, 'A': 0 })

    def test_kmers_of_varying_sizes(self):
        counts = { 'GTACAGCATACG': 54, 'A': 23, 'RYACY': -27 }
        dc = deep_copy_kmer_counts(counts)
        self.assertEqual(dc, { 'GTACAGCATACG': 54, 'A': 23, 'RYACY': -27 })
