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
    
    def test_exception(self):
        with self.assertRaises(TypeError):
            a = Rectangle(8)
            b = Rectangle()

class TestValidAttributes(unittest.TestCase):
    def test_valid_width(self):
        with self.assertRaises(TypeError):
            a = Rectangle('rect', 4)

        with self.assertRaises(ValueError):
            a = Rectangle(0, 4)
        
        with self.assertRaises(ValueError):
            a = Rectangle(-2, 4)

        
    def test_valid_height(self):
        with self.assertRaises(TypeError):
            a = Rectangle(4,'rect')

        with self.assertRaises(ValueError):
            a = Rectangle(4, 0)
        
        with self.assertRaises(ValueError):
            a = Rectangle(4, -2)
        

    def test_valid_x(self):
        with self.assertRaises(TypeError):
            a = Rectangle(2, 4, 3.4, 5)

        with self.assertRaises(ValueError):
            a = Rectangle(2, 4, -4, 5)


    def test_valid_y(self):
        with self.assertRaises(TypeError):
            a = Rectangle(2, 4, 5, 3.4)

        with self.assertRaises(ValueError):
            a = Rectangle(2, 4, 4, -5)

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(2, 4, 4, 5)

    def test_area(self):
        self.assertEqual(self.a.area(), 8)

    def test_update_args(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b.update(6)
        self.assertEqual(b.id, 6)

        b.update(6, 7)
        self.assertEqual(b.width, 7)

        b.update(6, 7, 8)
        self.assertEqual(b.height, 8)

        b.update(6, 7, 8, 9)
        self.assertEqual(b.x, 9)

        b.update(6, 7, 8, 9, 10)
        self.assertEqual(b.y, 10)

    def test_update_kwargs(self):
        b = Rectangle(1, 2, 3, 4, 7)
        b.update(8, 9, id=89, width=17)
        self.assertEqual(b.id, 8)
        self.assertEqual(b.width, 9)

        c = Rectangle(6, 7)
        c.update(height=31, y=8)
        self.assertEqual(c.height, 31)
        self.assertEqual(c.y, 8)

        d = Rectangle(6, 7)
        d.update(0, x=8)
        self.assertEqual(d.x, 8)


