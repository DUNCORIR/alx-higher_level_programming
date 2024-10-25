#!/usr/bin/python3
"""Unit tests for the update method of the Rectangle class with *args and **kwargs."""
import unittest
from models.rectangle import Rectangle

class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for the update method in the Rectangle class using **kwargs."""

    def test_update_height_with_kwargs(self):
        """Test updating height using **kwargs."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

    def test_update_width_x_with_kwargs(self):
        """Test updating width and x using **kwargs."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

    def test_update_multiple_attributes_with_kwargs(self):
        """Test updating multiple attributes using **kwargs."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)

    def test_update_order_with_kwargs(self):
        """Test the order of updates using **kwargs."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)

    def test_update_with_args_and_kwargs(self):
        """Test that *args takes precedence over **kwargs when both are present."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(5, 6, 7, 8, 9, x=1, y=2)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 9)

if __name__ == '__main__':
    unittest.main()
