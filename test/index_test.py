import unittest2 as unittest
from twisted.trial import unittest
from ipynb.fs.full.index import (name)

class TestVariables(unittest.TestCase):
    def test_variables_intro(self):
        self.assertEqual(name, 'bob')
