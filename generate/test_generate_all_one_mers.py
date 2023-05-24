import unittest

from .generate_all_one_mers import generate_all_one_mers


class TestGenerateAllOneMersFunction(unittest.TestCase):
    def test_including_IUPAC_codes(self):
        one_mers = generate_all_one_mers(IUPAC=True)
        self.assertIs(len(one_mers), 15)
        self.assertTrue('A' in one_mers)
        self.assertTrue('T' in one_mers)
        self.assertTrue('G' in one_mers)
        self.assertTrue('C' in one_mers)
        self.assertTrue('R' in one_mers)
        self.assertTrue('Y' in one_mers)
        self.assertTrue('S' in one_mers)
        self.assertTrue('W' in one_mers)
        self.assertTrue('K' in one_mers)
        self.assertTrue('M' in one_mers)
        self.assertTrue('B' in one_mers)
        self.assertTrue('D' in one_mers)
        self.assertTrue('H' in one_mers)
        self.assertTrue('V' in one_mers)
        self.assertTrue('N' in one_mers)

    def test_omitting_IUPAC_codes(self):
        one_mers = generate_all_one_mers(IUPAC=False)
        self.assertIs(len(one_mers), 4)
        # check the standard codes
        self.assertTrue('A' in one_mers)
        self.assertTrue('T' in one_mers)
        self.assertTrue('G' in one_mers)
        self.assertTrue('C' in one_mers)
        # check some IUPAC codes
        self.assertTrue('N' not in one_mers)
        self.assertTrue('R' not in one_mers)
        self.assertTrue('Y' not in one_mers)
