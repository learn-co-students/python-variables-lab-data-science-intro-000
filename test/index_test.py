import unittest2 as unittest
from ipynb.fs.full.index import (travel_month, number_of_weeks)

class TestVariables(unittest.TestCase):
    def test_travel_month(self):
        self.assertEqual(travel_month, 'January')
