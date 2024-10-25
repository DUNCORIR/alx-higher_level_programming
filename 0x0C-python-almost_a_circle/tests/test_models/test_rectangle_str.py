#!/usr/bin/python3
"""Unit tests for the __str__ method of the Rectangle class."""
import unittest
from models.rectangle import Rectangle

class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method in the Rectangle class."""

    def test_str_method(self):
        """Test if __str__ returns the correct string representation."""
        # Create a rectangle and check its string representation
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_str1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_str1)

        # Create another rectangle with different parameters
        r2 = Rectangle(5, 5, 1, 0, 7)
        expected_str2 = "[Rectangle] (7) 1/0 - 5/5"
        self.assertEqual(str(r2), expected_str2)

        # Test default x and y values
        r3 = Rectangle(3, 4)
        r3_id = r3.id  # Capture the id assigned automatically
        expected_str3 = f"[Rectangle] ({r3_id}) 0/0 - 3/4"
        self.assertEqual(str(r3), expected_str3)

if __name__ == '__main__':
    unittest.main()
