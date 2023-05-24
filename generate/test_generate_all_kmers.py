import unittest

from .generate_all_kmers import generate_all_kmers


class TestIncludingIUPACCodes(unittest.TestCase):
    def test_k_of_one(self):
        kmers = generate_all_kmers(k=1, IUPAC=True)
        self.assertEqual(len(kmers), 15)
        for kmer in kmers:
            self.assertEqual(len(kmer), 1)
        # just check some one-mers
        self.assertTrue('A' in kmers)
        self.assertTrue('N' in kmers)
        self.assertTrue('R' in kmers)

    def test_k_of_three(self):
        kmers = generate_all_kmers(k=3, IUPAC=True)
        self.assertEqual(len(kmers), 3375)
        for kmer in kmers:
            self.assertEqual(len(kmer), 3)
        # (just check some three-mers)
        # only standard codes
        self.assertTrue('ATG' in kmers)
        # only special IUPAC codes
        self.assertTrue('NRY' in kmers)
        # mix of standard and special IUPAC codes
        self.assertTrue('YGT' in kmers)

    def test_k_of_six(self):
        kmers = generate_all_kmers(k=6, IUPAC=True)
        self.assertEqual(len(kmers), 11390625)
        for kmer in kmers:
            self.assertEqual(len(kmer), 6)
        # (just check some six-mers)
        # only standard codes
        self.assertTrue('ATGCAT' in kmers)
        # only special IUPAC codes
        self.assertTrue('YYRRNV' in kmers)
        # mix of standard and special IUPAC codes
        self.assertTrue('TYRNAA' in kmers)


class TestOmittingIUPACCodes(unittest.TestCase):
    def test_k_of_one(self):
        kmers = generate_all_kmers(k=1, IUPAC=False)
        self.assertEqual(len(kmers), 4)
        self.assertTrue('A' in kmers)
        self.assertTrue('T' in kmers)
        self.assertTrue('G' in kmers)
        self.assertTrue('C' in kmers)
        # check some special IUPAC codes
        self.assertFalse('N' in kmers)
        self.assertFalse('R' in kmers)
        self.assertFalse('Y' in kmers)

    def test_k_of_three(self):
        kmers = generate_all_kmers(k=3, IUPAC=False)
        self.assertEqual(len(kmers), 64)
        for kmer in kmers:
            self.assertEqual(len(kmer), 3)
        # (just check some three-mers)
        # only standard codes
        self.assertTrue('AAA' in kmers)
        self.assertTrue('TGA' in kmers)
        self.assertTrue('AAC' in kmers)
        self.assertTrue('CAT' in kmers)
        self.assertTrue('TAG' in kmers)
        # containing some special IUPAC codes
        self.assertFalse('AAY' in kmers)
        self.assertFalse('NAN' in kmers)
        self.assertFalse('RRW' in kmers)

    def test_k_of_six(self):
        kmers = generate_all_kmers(k=6, IUPAC=False)
        self.assertEqual(len(kmers), 4096)
        for kmer in kmers:
            self.assertEqual(len(kmer), 6)
        # (just check some six-mers)
        # only standard codes
        self.assertTrue('ATGCAT' in kmers)
        self.assertTrue('TTCTGG' in kmers)
        self.assertTrue('GCAGCA' in kmers)
        self.assertTrue('TTACGA' in kmers)
        self.assertTrue('TTTGGG' in kmers)
        self.assertTrue('GCGCTA' in kmers)
        # containing some special IUPAC codes
        self.assertFalse('AANGCA' in kmers)
        self.assertFalse('NNNNNN' in kmers)
        self.assertFalse('RYRYWW' in kmers)
