import unittest

from count_kmers import count_kmers


class TestEmptySequence(unittest.TestCase):
    def test_k_of_one(self):
        counts = count_kmers(sequence='', k=1)
        self.assertEqual(counts, {})

    def test_k_of_three(self):
        counts = count_kmers(sequence='', k=3)
        self.assertEqual(counts, {})

    def test_k_of_ten(self):
        counts = count_kmers(sequence='', k=10)
        self.assertEqual(counts, {})


class TestSequencesOfLengthOne(unittest.TestCase):
    def test_k_of_one(self):
        counts = count_kmers(sequence='T', k=1)
        self.assertEqual(counts, { 'T': 1 })

    def test_k_of_five(self):
        counts = count_kmers(sequence='A', k=5)
        self.assertEqual(counts, {})


class TestLongerSequences(unittest.TestCase):
    def test_k_of_one(self):
        sequence = 'ATCGCGATGCTAGCTATA'
        counts = count_kmers(sequence=sequence, k=1)
        self.assertEqual(counts, {
            'A': 5,
            'T': 5,
            'G': 4,
            'C': 4,
        })

    def test_k_of_two(self):
        sequence = 'ACCGACGCATTATACGACTAGA'
        counts = count_kmers(sequence=sequence, k=2)
        self.assertEqual(counts, {
            'AC': 4,
            'CC': 1,
            'CG': 3,
            'GA': 3,
            'GC': 1,
            'CA': 1,
            'AT': 2,
            'TT': 1,
            'TA': 3,
            'CT': 1,
            'AG': 1,
        })

    def test_k_of_five(self):
        sequence = 'AACGGGCTCGAGGAACGCGCGCGCAACGCA'
        counts = count_kmers(sequence=sequence, k=5)
        self.assertEqual(counts, {
            'AACGG': 1,
            'ACGGG': 1,
            'CGGGC': 1,
            'GGGCT': 1,
            'GGCTC': 1,
            'GCTCG': 1,
            'CTCGA': 1,
            'TCGAG': 1,
            'CGAGG': 1,
            'GAGGA': 1,
            'AGGAA': 1,
            'GGAAC': 1,
            'GAACG': 1,
            'AACGC': 2,
            'ACGCG': 1,
            'CGCGC': 3,
            'GCGCG': 2,
            'GCGCA': 1,
            'CGCAA': 1,
            'GCAAC': 1,
            'CAACG': 1,
            'ACGCA': 1,
        })

    def test_k_equal_to_sequence_length(self):
        sequence = 'AGCTAGCGACGAGAGACC'
        counts = count_kmers(sequence=sequence, k=len(sequence))
        self.assertEqual(counts, {
            'AGCTAGCGACGAGAGACC': 1,
        })

    def test_k_greater_than_sequence_length(self):
        sequence = 'AGCTCGAAGAGCGCC'
        counts = count_kmers(sequence=sequence, k=1000000)
        self.assertEqual(counts, {})
