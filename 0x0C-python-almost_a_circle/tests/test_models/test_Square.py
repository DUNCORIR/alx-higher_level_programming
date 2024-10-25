#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle

class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_square_initialization(self):
        """Test initialization of a Square instance."""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(3, 2, 1, 42)
        self.assertEqual(s2.id, 42)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 3)
        self.assertBEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)

    def test_square_area(self):
        """Test the area method of the Square."""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(3)
        self.assertEqual(s2.area(), 9)

    def test_square_str(self):
        """Test the __str__ method of the Square."""
        s1 = Square(5, 2, 3, 45)
        self.assertEqual(str(s1), "[Square] (45) 2/3 - 5")

    def test_square_display(self):
        """Test the display method of the Square."""
        s1 = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        s2 = Square(2, 1, 1)
        expected_output = "\n ###\n ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_square_size_setter_getter(self):
        """Test size setter and getter for Square."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaises(TypeError):
            s1.size = "invalid"
        with self.assertRaises(ValueError):
            s1.size = -10

    def test_inheritance_from_rectangle(self):
        """Test that Square is indeed a subclass of Rectangle."""
        s1 = Square(5)
        self.assertIsInstance(s1, Rectangle)

if __name__ == '__main__':
    unittest.main()
