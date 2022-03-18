import unittest
from models.make import Make

class TestMake(unittest.TestCase):

    def setUp(self):
        self.make = Make("Canon")

    def test_make_has_name(self):
        self.assertEqual("Canon", self.make.name)