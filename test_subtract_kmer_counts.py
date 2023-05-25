import unittest

from subtract_kmer_counts import subtract_kmer_counts


class TestEmptyKmerCountsDicts(unittest.TestCase):
    def test_two_empty_kmer_counts_dicts(self):
        subtracted = subtract_kmer_counts({}, {})
        self.assertEqual(subtracted, {})

    def test_empty_first_kmer_counts_dict(self):
        counts2 = { 'A': 5, 'GG': 6 }
        subtracted = subtract_kmer_counts({}, counts2)
        self.assertEqual(subtracted, { 'A': -5, 'GG': -6 })

    def test_empty_second_kmer_counts_dict(self):
        counts1 = { 'G': 57, 'C': 3 }
        subtracted = subtract_kmer_counts(counts1, {})
        self.assertEqual(subtracted, { 'G': 57, 'C': 3 })


class TestSharedKmers(unittest.TestCase):
    def test_one_shared_kmer(self):
        counts1 = { 'AC': 8 }
        counts2 = { 'AC': 15 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'AC': -7 })

    def test_three_shared_kmers(self):
        counts1 = { 'a': 10, 'b': 23, 'c': 84 }
        counts2 = { 'b': 25, 'c': 3, 'a': 28 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'a': -18, 'b': -2, 'c': 81 })


class TestUnsharedKmers(unittest.TestCase):
    def test_unshared_kmers_in_first_dict(self):
        counts1 = { 'AA': 6, 'BC': 24, 'GT': 45 }
        counts2 = { 'AA': 3 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'AA': 3, 'BC': 24, 'GT': 45 })

    def test_unshared_kmers_in_second_dict(self):
        counts1 = { 'G': 56 }
        counts2 = { 'G': 24, 'C': 11, 'ACC': 9 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'G': 32, 'C': -11, 'ACC': -9 })


class TestNegativeCounts(unittest.TestCase):
    def test_negative_counts_in_first_dict(self):
        counts1 = { 'C': -5, 'ACCA': -11 }
        counts2 = { 'C': 5, 'ACCA': 24 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'C': -10, 'ACCA': -35 })

    def test_negative_counts_in_second_dict(self):
        counts1 = { 'GG': 54, 'C': 108 }
        counts2 = { 'GG': -19, 'C': -33 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'GG': 73, 'C': 141 })

    def test_negative_counts_in_both_dicts(self):
        counts1 = { 'G': -190, 'GGG': -3 }
        counts2 = { 'G': -12, 'GGG': -59 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'G': -178, 'GGG': 56 })


class TestCountsOfZero(unittest.TestCase):
    def test_counts_of_zero_in_both_dicts(self):
        counts1 = { 'A': 0, 'R': 0 }
        counts2 = { 'A': 0, 'Y': 0 }
        subtracted = subtract_kmer_counts(counts1, counts2)
        self.assertEqual(subtracted, { 'A': 0, 'R': 0, 'Y': 0 })
