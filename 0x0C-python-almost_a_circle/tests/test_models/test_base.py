import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_id_int(self):
        a = Base(2)
        self.assertEqual(a.id, 2)

    def test_id_none(self):
        b = Base()
        self.assertEqual(b.id, 1)

class TestJsonBase(unittest.TestCase):
    def test_json_type(self):
        a = Square(3)
        self.assertIs(type(Base.to_json_string([a.to_dictionary()])), str)

    def test_json_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

