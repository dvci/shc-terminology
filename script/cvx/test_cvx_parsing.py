import unittest
from cvx_parsing import retrieve_new_cvx

class TestCVXParsing(unittest.TestCase):

    def test_retrieve_new_cvx(self):

        actual = retrieve_new_cvx()
        self.assertEqual(actual['208']['short-description'], "COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose")
    