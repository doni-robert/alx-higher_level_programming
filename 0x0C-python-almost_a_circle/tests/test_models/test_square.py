import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestSquareInitialization(unittest.TestCase):
    def setUp(self):
        self.a = Square(1, 2, 3, 4)
        self.b = Square(7)

    def test_subclass_base(self):
        self.assertIsInstance(self.a, Base)

    def test_subclass_rectangle(self):
        self.assertIsInstance(self.a, Rectangle)

    def test_width_getter(self):
        self.assertEqual(self.a.width, 1)

    def test_width_setter(self):
        self.a.width = 7
        self.assertEqual(self.a.width, 7)

    def test_height_getter(self):
        self.assertEqual(self.b.height, 7)

    def test_height_setter(self):
        self.a.height = 8
        self.assertEqual(self.a.height, 8)

    def test_size_getter(self):
        c = Square(9)
        self.assertEqual(c.size, 9)

    def test_size_setter(self):
        c = Square(9)
        c.size = 8
        self.assertEqual(c.size, 8)
    
    def test_x_getter(self):
        self.assertEqual(self.a.x, 2)

    def test_x_setter(self):
        self.a.x = 9
        self.assertEqual(self.a.x, 9)

    def test_y_getter(self):
        self.assertEqual(self.a.y, 3)

    def test_y_setter(self):
        self.a.y = 10
        self.assertEqual(self.a.y, 10)

    def test_id(self):
        self.assertEqual(self.a.id, 4)

    def test_default_values(self):
        self.assertEqual(self.b.x, 0)
        self.assertEqual(self.b.y, 0)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            b = Square()

class TestValidAttributes(unittest.TestCase):
    def test_valid_size_int(self):
        with self.assertRaises(TypeError):
            a = Square('sqr')

    def test_valid_size_zero(self):
        with self.assertRaises(ValueError):
            a = Square(0)

    def test_valid_size_negative(self):
        with self.assertRaises(ValueError):
            a = Square(-2)

    def test_valid_x_int(self):
        with self.assertRaises(TypeError):
            a = Square(2, 3.4, 5)

    def test_valid_x_negative(self):
        with self.assertRaises(ValueError):
            a = Square(2, -4, 5)

    def test_valid_y_int(self):
        with self.assertRaises(TypeError):
            a = Square(2, 5, 3.4)

    def test_valid_y_negative(self):
        with self.assertRaises(ValueError):
            a = Square(2, 4, -5)

class TestArea(unittest.TestCase):
    def test_area(self):
        a = Square(2, 4, 5)
        self.assertEqual(a.area(), 4)

class TestStr(unittest.TestCase):
    def test_str(self):
        a = Square(2, 4, 4, 5)
        self.assertEqual(str(a), "[Square] (5) 4/4 - 2")

class TestArgs(unittest.TestCase):
    def test_one_arg(self):
        b = Square(1, 2, 3, 4)
        b.update(6)
        self.assertEqual(b.id, 6)

    def test_two_args(self):
        b = Square(1, 2, 3, 4)
        b.update(6, 7)
        self.assertEqual(b.size, 7)

    def test_three_args(self):
        b = Square(1, 2, 3, 4)
        b.update(6, 7, 8)
        self.assertEqual(b.x, 8)

    def test_four_args(self):
        b = Square(1, 2, 3, 4)
        b.update(6, 7, 8, 9)
        self.assertEqual(b.y, 9)

    def test_no_args(self):
        b = Square(1, 2, 3, 4)
        b.update()
        self.assertEqual(b.y, 3)
        self.assertEqual(b.size, 1)

    def test_type_args(self):
        with self.assertRaises(TypeError):
            c = Square(6, 7)
            c.update(9, 3, 'tall', 8)

class TestKwargs(unittest.TestCase):
    def test_args_kwargs(self):
        b = Square(1, 2, 3, 4)
        b.update(8, 9, id=89, size=17)
        self.assertEqual(b.id, 8)
        self.assertEqual(b.size, 9)

    def test_just_kwargs(self):
        c = Square(6,)
        c.update(size=31, y=8)
        self.assertEqual(c.size, 31)
        self.assertEqual(c.y, 8)

    def test_type_kwargs(self):
        with self.assertRaises(TypeError):
            c = Square(6, 7)
            c.update(size='tall', y=8)

    def test_empty_args(self):
        c = Square(6, 7)
        args = []
        c.update(*args, size=31, y=8)
        self.assertEqual(c.size, 31)
        self.assertEqual(c.y, 8)

class TestToDictionary(unittest.TestCase):
    def test_dict_repr(self):
        a = Square(1, 3, 4, 7)
        a_dict = a.to_dictionary()
        self.assertEqual(a_dict, {'x': 3, 'y': 4, 'id': 7, 'size':1})

    def test_dict_type(self):
        a = Rectangle(1, 3, 4, 7)
        a_dict = a.to_dictionary()
        self.assertEqual(type(a_dict), dict)

