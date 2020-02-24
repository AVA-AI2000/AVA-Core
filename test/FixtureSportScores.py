import unittest
import sys

sys.path.append('../src/skills')

import SportScores


class TestSportScores(unittest.TestCase):
    def test_load_api(self):
        funct, keys = SportScores.load_api()
        self.assertEqual(keys, ['ku', 'score'])
        self.assertEqual(funct, SportScores.main)

    def test_main(self):
        ret_str = SportScores.main({}, [])
        self.assertEqual(ret_str, "WIN")
