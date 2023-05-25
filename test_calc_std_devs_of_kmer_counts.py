import unittest

from calc_std_devs_of_kmer_counts import calc_std_devs_of_kmer_counts


class TestEmpty(unittest.TestCase):
    def test_an_empty_list_of_kmer_counts_dicts(self):
        std_devs = calc_std_devs_of_kmer_counts([])
        self.assertEqual(std_devs, {})

    def test_one_empty_kmer_counts_dict(self):
        std_devs = calc_std_devs_of_kmer_counts([{}])
        self.assertEqual(std_devs, {})

    def test_three_empty_kmer_counts_dicts(self):
        std_devs = calc_std_devs_of_kmer_counts([{}, {}, {}])
        self.assertEqual(std_devs, {})


class TestKmers(unittest.TestCase):
    def test_one_kmer_shared_among_all_dicts(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'G': 5 })
        kmer_counts_list.append({ 'G': 2 })
        kmer_counts_list.append({ 'G': 12 })
        std_devs = calc_std_devs_of_kmer_counts(kmer_counts_list)
        self.assertEqual(std_devs, { 'G': 4.189935029992179 })

    def test_three_kmers_shared_among_all_dicts(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'a': 2, 'NYN': 12, 'RR': 20 })
        kmer_counts_list.append({ 'a': 0, 'NYN': 9, 'RR': 19 })
        kmer_counts_list.append({ 'a': 3, 'NYN': 100, 'RR': 16 })
        std_devs = calc_std_devs_of_kmer_counts(kmer_counts_list)
        self.assertEqual(len(std_devs), 3)
        self.assertAlmostEqual(std_devs['a'], 1.247219128924647)
        self.assertAlmostEqual(std_devs['NYN'], 42.20847729491737)
        self.assertAlmostEqual(std_devs['RR'], 1.699673171197595)


class TestUnsharedKmers(unittest.TestCase):
    def test_no_shared_kmers(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'A': 2 })
        kmer_counts_list.append({ 'b': 20 })
        kmer_counts_list.append({ 'R': 5 })
        kmer_counts_list.append({ 'N': 88 })
        std_devs = calc_std_devs_of_kmer_counts(kmer_counts_list)
        self.assertEqual(len(std_devs), 4)
        self.assertAlmostEqual(std_devs['A'], 0.8660254037844386)
        self.assertAlmostEqual(std_devs['b'], 8.660254037844387)
        self.assertAlmostEqual(std_devs['R'], 2.165063509461097)
        self.assertAlmostEqual(std_devs['N'], 38.1051177665153)

    def test_kmers_that_vary_in_how_much_they_are_shared(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'NN': 24, 'B': 11 })
        kmer_counts_list.append({ 'B': 2, 'RRR': 100 })
        kmer_counts_list.append({})
        kmer_counts_list.append({ 'A': 22, 'NN': 50 })
        kmer_counts_list.append({ 'NN': 57, 'Q': 59 })
        std_devs = calc_std_devs_of_kmer_counts(kmer_counts_list)
        self.assertEqual(len(std_devs), 5)
        self.assertAlmostEqual(std_devs['NN'], 24.053274205396654)
        self.assertAlmostEqual(std_devs['B'], 4.2708313008125245)
        self.assertAlmostEqual(std_devs['RRR'], 40.0)
        self.assertAlmostEqual(std_devs['A'], 8.8)
        self.assertAlmostEqual(std_devs['Q'], 23.6)


class TestNegativeCountsAndCountsOfZero(unittest.TestCase):
    def test_a_mix_of_positive_and_negative_counts_and_counts_of_zero(self):
        kmer_counts_list = []
        kmer_counts_list.append({ 'A': 24, 'B': -88, 'C': 0 })
        kmer_counts_list.append({ 'N': 3, 'B': 12, 'C': 44 })
        kmer_counts_list.append({ 'A': -2, 'C': -9 })
        std_devs = calc_std_devs_of_kmer_counts(kmer_counts_list)
        self.assertEqual(len(std_devs), 4)
        self.assertAlmostEqual(std_devs['A'], 11.8133634311129)
        self.assertAlmostEqual(std_devs['B'], 44.58200932613463)
        self.assertAlmostEqual(std_devs['C'], 23.156472577277878)
        self.assertAlmostEqual(std_devs['N'], 1.4142135623730951)
