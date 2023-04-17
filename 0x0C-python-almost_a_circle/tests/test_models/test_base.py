import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id(self):
        a = Base(2)
        b = Base()
        self.assertEqual(a.id, 2)
        self.assertEqual(b.id, 1)

