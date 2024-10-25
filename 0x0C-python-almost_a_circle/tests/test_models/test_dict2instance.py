#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):

    def test_create_rectangle(self):
        """Test create method for Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        # Ensure that r2 is an instance of Rectangle
        self.assertIsInstance(r2, Rectangle)
        
        # Ensure that r2 has the same attributes as r1
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)

        # Ensure r1 and r2 are not the same instance
        self.assertIsNot(r1, r2)

        # Ensure that r1 and r2 are equal in terms of attributes
        self.assertEqual(r1, r2)

    def test_create_square(self):
        """Test create method for Square."""
        s1 = Square(5, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        # Ensure that s2 is an instance of Square
        self.assertIsInstance(s2, Square)

        # Ensure that s2 has the same attributes as s1
        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)

        # Ensure s1 and s2 are not the same instance
        self.assertIsNot(s1, s2)

        # Ensure that s1 and s2 are equal in terms of attributes
        self.assertEqual(s1, s2)

if __name__ == "__main__":
    unittest.main()
