import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_int(self):
        a = Base(2)
        self.assertEqual(a.id, 2)

    def test_id_none(self):
        b Base()
        self.assertEqual(b.id, 1)

