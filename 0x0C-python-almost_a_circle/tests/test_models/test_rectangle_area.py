#!/usr/bin/python3
"""Unit tests for the area method of the Rectangle class."""
import unittest
from models.rectangle import Rectangle

class TestRectangleArea(unittest.TestCase):
    """Tests for the area method in the Rectangle class."""

    def test_area_small_values(self):
        """Test the area calculation with small integer values."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7)
        self.assertEqual(r3.area(), 56)

    def test_area_large_values(self):
        """Test the area calculation with larger values."""
        r1 = Rectangle(100, 200)
        self.assertEqual(r1.area(), 20000)

        r2 = Rectangle(999, 999)
        self.assertEqual(r2.area(), 998001)

    def test_area_edge_case(self):
        """Test edge cases where the area calculation may be tricky."""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.area(), 1)

        r2 = Rectangle(10, 1)
        self.assertEqual(r2.area(), 10)

if __name__ == '__main__':
    unittest.main()
