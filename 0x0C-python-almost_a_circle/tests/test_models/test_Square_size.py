#!/usr/bin/python3
"""Unit tests for the Square class - size property."""
import unittest
from models.square import Square

class TestSquareSize(unittest.TestCase):
    """Tests for the size getter and setter in the Square class."""

    def test_square_size_getter(self):
        """Test that size getter returns the correct value."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(10, 2, 3)
        self.assertEqual(s2.size, 10)

    def test_square_size_setter(self):
        """Test that size setter updates width and height correctly."""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.size, 10)

    def test_square_size_validation(self):
        """Test that setting size validates the input correctly."""
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "9"  # Should raise a TypeError

        with self.assertRaises(ValueError):
            s1.size = -5  # Should raise a ValueError

        with self.assertRaises(ValueError):
            s1.size = 0  # Should raise a ValueError

    def test_square_size_exception_messages(self):
        """Check that exception messages match those for width in Rectangle."""
        s1 = Square(5)

        with self.assertRaises(TypeError) as e:
            s1.size = "invalid"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = -5
        self.assertEqual(str(e.exception), "width must be > 0")

if __name__ == '__main__':
    unittest.main()
