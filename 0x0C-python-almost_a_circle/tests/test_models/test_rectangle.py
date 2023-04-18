import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleInitialization(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(2, 3, 4, 5, 6)
        self.b = Rectangle(7, 8)

    def test_subclass(self):
        self.assertIsInstance(Rectangle(3, 4), Base)

    def test_width_getter(self):
        self.assertEqual(self.a.width, 2)

    def test_width_setter(self):
        self.a.width = 7
        self.assertEqual(self.a.width, 7)

    def test_height_getter(self):
        self.assertEqual(self.a.height, 3)

    def test_height_setter(self):
        self.a.height = 8
        self.assertEqual(self.a.height, 8)

    def test_x_getter(self):
        self.assertEqual(self.a.x, 4)

    def test_x_setter(self):
        self.a.x = 9
        self.assertEqual(self.a.x, 9)

    def test_y_getter(self):
        self.assertEqual(self.a.y, 5)

    def test_y_setter(self):
        self.a.y = 10
        self.assertEqual(self.a.y, 10)

    def test_id(self):
        self.assertEqual(self.a.id, 6)

    def test_default_values(self):
        b = Rectangle(7, 8)

        self.assertEqual(b.x, 0)
        self.assertEqual(b.y, 0)
    
    def test_one_arg(self):
        with self.assertRaises(TypeError):
            a = Rectangle(8)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            b = Rectangle()


class TestValidAttributes(unittest.TestCase):
    def test_valid_width_int(self):
        with self.assertRaises(TypeError):
            a = Rectangle('rect', 4)

    def test_valid_width_zero(self):
        with self.assertRaises(ValueError):
            a = Rectangle(0, 4)
    
    def test_valid_width_negative(self):
        with self.assertRaises(ValueError):
            a = Rectangle(-2, 4)

    def test_valid_height_int(self):
        with self.assertRaises(TypeError):
            a = Rectangle(4,'rect')

    def test_valid_height_zero(self):
        with self.assertRaises(ValueError):
            a = Rectangle(4, 0)
        
    def test_valid_height_negative(self):
        with self.assertRaises(ValueError):
            a = Rectangle(4, -2)
        
    def test_valid_x_int(self):
        with self.assertRaises(TypeError):
            a = Rectangle(2, 4, 3.4, 5)

    def test_valid_x_negative(self):
        with self.assertRaises(ValueError):
            a = Rectangle(2, 4, -4, 5)
    
    def test_valid_y_int(self):
        with self.assertRaises(TypeError):
            a = Rectangle(2, 4, 5, 3.4)

    def test_valid_y_negative(self):
        with self.assertRaises(ValueError):
            a = Rectangle(2, 4, 4, -5)
    
class TestArea(unittest.TestCase):
    def test_area(self):
        a = Rectangle(2, 4, 4, 5)
        self.assertEqual(a.area(), 8)

class TestStr(unittest.TestCase):
    def test_str(self):
        a = Rectangle(2, 4, 4, 5, 12)
        self.assertEqual(str(a), "[Rectangle] (12) 4/5 - 2/4")

class TestArgs(unittest.TestCase):
    def test_one_arg(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b.update(6)
        self.assertEqual(b.id, 6)
    
    def test_two_args(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b.update(6, 7)
        self.assertEqual(b.width, 7)

    def test_three_args(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b.update(6, 7, 8)
        self.assertEqual(b.height, 8)

    def test_four_args(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b.update(6, 7, 8, 9)
        self.assertEqual(b.x, 9)

    def test_five_args(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b.update(6, 7, 8, 9, 10)
        self.assertEqual(b.y, 10)

    def test_no_args(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b.update()
        self.assertEqual(b.y, 4)
        self.assertEqual(b.width, 1)

    def test_type_args(self):
        with self.assertRaises(TypeError):
            c = Rectangle(6, 7)
            c.update(5, 'rect', 9)
    
class TestKwargs(unittest.TestCase):
    def test_args_kwargs(self):
        b = Rectangle(1, 2, 3, 4, 7)
        b.update(8, 9, id=89, width=17)
        self.assertEqual(b.id, 8)
        self.assertEqual(b.width, 9)

    def test_just_kwargs(self):
        c = Rectangle(6, 7)
        c.update(height=31, y=8)
        self.assertEqual(c.height, 31)
        self.assertEqual(c.y, 8)
    
    def test_value_type_kwargs(self):
        with self.assertRaises(TypeError):
            c = Rectangle(6, 7)
            c.update(height='tall', y=8)

    def test_empty_args(self):
        c = Rectangle(6, 7)
        args = []
        c.update(*args, height=31, y=8)
        self.assertEqual(c.height, 31)
        self.assertEqual(c.y, 8)

