import unittest

from calc_mean_kmer_counts import calc_mean_kmer_counts


class TestEmpty(unittest.TestCase):
    def test_empty_list_of_kmer_counts_dicts(self):
        means = calc_mean_kmer_counts([])
        self.assertEqual(means, {})

    def test_one_empty_kmer_counts_dict(self):
        means = calc_mean_kmer_counts([{}])
        self.assertEqual(means, {})

    def test_three_empty_kmer_counts_dicts(self):
        means = calc_mean_kmer_counts([{}, {}, {}])
        self.assertEqual(means, {})

    def test_when_only_some_kmer_counts_dicts_are_empty(self):
        kmer_counts_list = []
        kmer_counts_list.append({})
        kmer_counts_list.append({ 'AA': 2, 'G': 8 })
        kmer_counts_list.append({})
        kmer_counts_list.append({ 'C': 55, 'G': 49 })
        kmer_counts_list.append({})
        means = calc_mean_kmer_counts(kmer_counts_list)
        self.assertEqual(means, { 'AA': 2 / 5, 'C': 55 / 5, 'G': 57 / 5 })


class TestSharedKmers(unittest.TestCase):
    def test_one_kmer_shared_among_all_dicts(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'NYN': 23 })
        kmer_counts_list.append({ 'NYN': 2 })
        kmer_counts_list.append({ 'NYN': 79 })
        means = calc_mean_kmer_counts(kmer_counts_list)
        self.assertEqual(means, { 'NYN': 104 / 3 })

    def test_three_kmers_shared_among_all_dicts(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'C': 24, 'N': 9, 'AAC': 23 })
        kmer_counts_list.append({ 'C': 23, 'N': 1, 'AAC': 3 })
        kmer_counts_list.append({ 'C': 5, 'N': 19, 'AAC': 97 })
        kmer_counts_list.append({ 'C': 11, 'N': 2, 'AAC': 104 })
        means = calc_mean_kmer_counts(kmer_counts_list)
        self.assertEqual(means, { 'C': 63 / 4, 'N': 31 / 4, 'AAC': 227 / 4 })


class TestUnsharedKmers(unittest.TestCase):
    def test_when_no_kmers_are_shared(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'B': 45 })
        kmer_counts_list.append({ 'CCC': 49 })
        kmer_counts_list.append({ 'a': 9 })
        means = calc_mean_kmer_counts(kmer_counts_list)
        self.assertEqual(means, { 'B': 45 / 3, 'CCC': 49 / 3, 'a': 9 / 3 })

    def test_when_kmers_vary_in_how_much_they_are_shared(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'B': 54 })
        kmer_counts_list.append({ 'B': 88, 'C': 24 })
        kmer_counts_list.append({ 'D': 66 })
        kmer_counts_list.append({ 'C': 21 })
        means = calc_mean_kmer_counts(kmer_counts_list)
        self.assertEqual(means, { 'B': 142 / 4, 'C': 45 / 4, 'D': 66 / 4 })


class TestNegativeCounts(unittest.TestCase):
    def test_a_mix_of_positive_and_negative_counts(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'C': -57, 'RRY': 2, 'N': 4 })
        kmer_counts_list.append({ 'C': 30, 'RRY': -99 })
        kmer_counts_list.append({ 'N': 8 })
        kmer_counts_list.append({ 'RRY': 6 })
        means = calc_mean_kmer_counts(kmer_counts_list)
        self.assertEqual(means, { 'C': -27 / 4, 'RRY': -91 / 4, 'N': 12 / 4})


class TestCountsOfZero(unittest.TestCase):
    def test_a_mix_of_zero_and_non_zero_counts(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'A': 0, 'GG': 2, 'CR': 28 })
        kmer_counts_list.append({ 'A': 0, 'GG': 0 })
        kmer_counts_list.append({ 'CR': 0 })
        kmer_counts_list.append({ 'GG': 52 })
        means = calc_mean_kmer_counts(kmer_counts_list)
        self.assertEqual(means, { 'A': 0, 'GG': 54 / 4, 'CR': 28 / 4 })
