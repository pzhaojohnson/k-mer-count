import unittest

from sum_kmer_counts import sum_kmer_counts


class TestEmptyKmerCountsDicts(unittest.TestCase):
    def test_both_kmer_counts_dicts_are_empty(self):
        sum_ = sum_kmer_counts({}, {})
        self.assertEqual(sum_, {})

    def test_empty_kmer_counts1_dict(self):
        kmer_counts2 = { 'ATG': 2, 'AA': 5 }
        sum_ = sum_kmer_counts({}, kmer_counts2)
        self.assertEqual(sum_, { 'ATG': 2, 'AA': 5 })

    def test_empty_kmer_counts2_dict(self):
        kmer_counts1 = { 'T': 55, 'C': 1 }
        sum_ = sum_kmer_counts(kmer_counts1, {})
        self.assertEqual(sum_, { 'T': 55, 'C': 1 })


class TestSharedKmers(unittest.TestCase):
    def test_one_shared_kmer(self):
        kmer_counts1 = { 'ATTG': 23 }
        kmer_counts2 = { 'ATTG': 17 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'ATTG': 40 })

    def test_three_shared_kmers(self):
        kmer_counts1 = { 'AG': 2, 'C': 101, 'TTT': 5 }
        kmer_counts2 = { 'C': 2, 'AG': 57, 'TTT': 3 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'AG': 59, 'C': 103, 'TTT': 8 })


class TestUnsharedKmers(unittest.TestCase):
    def test_unshared_kmers_in_dict1(self):
        kmer_counts1 = { 'AAA': 2, 'GT': 5, 'CC': 4 }
        kmer_counts2 = { 'CC': 5 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'AAA': 2, 'GT': 5, 'CC': 9 })

    def test_unshared_kmers_in_dict2(self):
        kmer_counts1 = { 'GTG': 3 }
        kmer_counts2 = { 'GTG': 2, 'AG': 55, 'CTG': 3, 'A': 2 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'GTG': 5, 'AG': 55, 'CTG': 3, 'A': 2 })


class TestNegativeCounts(unittest.TestCase):
    def test_positive_first_count(self):
        kmer_counts1 = { 'C': 22 }
        kmer_counts2 = { 'C': -9 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'C': 13 })

    def test_positive_second_count(self):
        kmer_counts1 = { 'TT': -42 }
        kmer_counts2 = { 'TT': 18 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'TT': -24 })

    def test_both_counts_are_negative(self):
        kmer_counts1 = { 'W': -21 }
        kmer_counts2 = { 'W': -7 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'W': -28 })

    def test_no_first_count(self):
        kmer_counts2 = { 'RW': -102 }
        sum_ = sum_kmer_counts({}, kmer_counts2)
        self.assertEqual(sum_, { 'RW': -102 })

    def test_no_second_count(self):
        kmer_counts1 = { 'NNN': -23 }
        sum_ = sum_kmer_counts(kmer_counts1, {})
        self.assertEqual(sum_, { 'NNN': -23 })


class TestCountsOfZero(unittest.TestCase):
    def test_positive_and_negative_first_counts(self):
        kmer_counts1 = { 'R': 2, 'Y': -35 }
        kmer_counts2 = { 'R': 0, 'Y': 0 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'R': 2, 'Y': -35 })

    def test_positive_and_negative_second_counts(self):
        kmer_counts1 = { 'A': 0, 'GG': 0 }
        kmer_counts2 = { 'A': 5, 'GG': -6 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'A': 5, 'GG': -6 })

    def test_two_counts_of_zero(self):
        kmer_counts1 = { 'T': 0 }
        kmer_counts2 = { 'T': 0 }
        sum_ = sum_kmer_counts(kmer_counts1, kmer_counts2)
        self.assertEqual(sum_, { 'T': 0 })

    def test_no_first_count(self):
        kmer_counts2 = { 'GG': 0 }
        sum_ = sum_kmer_counts({}, kmer_counts2)
        self.assertEqual(sum_, { 'GG': 0 })

    def test_no_second_count(self):
        kmer_counts1 = { 'A': 0 }
        sum_ = sum_kmer_counts(kmer_counts1, {})
        self.assertEqual(sum_, { 'A': 0 })
